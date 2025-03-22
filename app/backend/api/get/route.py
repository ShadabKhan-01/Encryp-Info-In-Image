from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from utils import extract_binary_from_pixels, binary_to_text

app = Flask(__name__)
CORS(app)

@app.route("/get", methods=["POST"])
def process_data():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Missing images"}), 400

    # Get and read images
    image1 = request.files["image1"]
    image2 = request.files["image2"]

    image_np_1 = np.frombuffer(image1.read(), np.uint8)  # Convert image file to NumPy array
    image_np_2 = np.frombuffer(image2.read(), np.uint8)  # Convert image file to NumPy array

    img_1 = cv2.imdecode(image_np_1, cv2.IMREAD_COLOR)  # Decode image as BGR
    img_2 = cv2.imdecode(image_np_2, cv2.IMREAD_COLOR)  # Decode image as BGR

    img_rgb_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)  # Convert to RGB
    img_rgb_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Convert RGB values to list of lists
    rgb_pixels_1 = img_rgb_1.tolist()
    rgb_pixels_2 = img_rgb_2.tolist()

    try:
        # Extract binary and convert to text
        extracted_binary = extract_binary_from_pixels(rgb_pixels_1, rgb_pixels_2)
        text = binary_to_text(extracted_binary)

        print("Extracted Binary:", extracted_binary)
        print("Decoded Text:", text)
        
        return jsonify({"Final_text": text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error while processing images"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)

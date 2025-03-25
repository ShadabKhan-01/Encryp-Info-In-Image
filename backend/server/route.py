from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
from server.utils import manipulate_pixels # Import the function
from utils import save_image
from utils import extract_binary_from_pixels, binary_to_text

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/generate", methods=["POST"])
def process_generate():
    if "image" not in request.files or "text" not in request.form:
        return jsonify({"error": "Missing image or text"}), 400

    # Get text and image
    text = request.form["text"]
    image = request.files["image"]

    print("Image and Text Recived for Genrate")

    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Convert image to RGB pixel array
    image_np = np.frombuffer(image.read(), np.uint8)  # Convert image file to NumPy array
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)  # Decode image as BGR
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Convert RGB values to list of lists
    rgb_pixels = img_rgb.tolist()
    
    # Call the function to manipulate the pixels
    modified_pixels = manipulate_pixels(rgb_pixels, binary_text)

    # Convert image back to Base64 for display on frontend
    modified_image_base64 = save_image(modified_pixels)

    # Return data as JSON
    return jsonify({
        "image_base64": modified_image_base64
    })


@app.route("/get", methods=["POST"])
def process_get():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Missing images"}), 400

    # Get and read images
    image1 = request.files["image1"]
    image2 = request.files["image2"]

    print("2 images Recived for Get")

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
        
        return jsonify({"Final_text": text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error while processing images"}), 500




if __name__ == "__main__":
    app.run(debug=True, port=5000)

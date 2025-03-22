from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
from utils import manipulate_pixels  # Import the function
from utils import save_image

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/generate", methods=["POST"])
def process_data():
    if "image" not in request.files or "text" not in request.form:
        return jsonify({"error": "Missing image or text"}), 400

    # Get text and image
    text = request.form["text"]
    image = request.files["image"]

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)

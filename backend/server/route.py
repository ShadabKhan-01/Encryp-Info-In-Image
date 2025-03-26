from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
import gc
from server.utils import manipulate_pixels, save_image, extract_binary_from_pixels, binary_to_text

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://imagecrypt.vercel.app/","https://encryp-info-in-image-git-main-shadabkhan-01s-projects.vercel.app/","https://encryp-info-in-image-shadabkhan-01s-projects.vercel.app/"]}})  # Enable CORS for frontend-backend communication

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 5 MB

### ------------------- IMAGE PROCESSING UTILITIES ------------------- ###

def read_and_decode_image(image):
    """Read and decode an image efficiently with error handling."""
    # Check if the image exceeds the max size
    image.seek(0, 2)  # Move to the end to get size
    image_size = image.tell()
    image.seek(0)  # Move back to the start

    if image_size > MAX_IMAGE_SIZE:
        raise ValueError("Image size exceeds the limit of 10 MB")

    # Read and decode image using NumPy and OpenCV
    image_np = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Invalid image format")

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Clean up memory
    del image_np, img
    gc.collect()

    return img_rgb

def cleanup_images(*images):
    """Release memory explicitly after image processing."""
    for image in images:
        del image
    gc.collect()


### ------------------- ROUTES ------------------- ###
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

    # Read and decode image
    img_rgb = read_and_decode_image(image)

    # Convert RGB values to list of lists
    rgb_pixels = img_rgb.tolist()
    
    # Call the function to manipulate the pixels
    modified_pixels = manipulate_pixels(rgb_pixels, binary_text)

    del binary_text, text, rgb_pixels
    gc.collect()

    # Convert image back to Base64 for display on frontend
    modified_image_base64 = save_image(modified_pixels)

    # Clean up memory after processing
    cleanup_images(img_rgb, modified_pixels)

    # Return data as JSON
    return jsonify({
        "image_base64": modified_image_base64
    })


@app.route("/get", methods=["POST"])
def process_get():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Missing images"}), 400

    try:
        # Get and read images
        image1 = request.files["image1"]
        image2 = request.files["image2"]

        print("2 images Recived for Get")

        img_rgb_1 = read_and_decode_image(image1)
        img_rgb_2 = read_and_decode_image(image2)

        del image1, image2
        gc.collect()

        # Convert RGB values to list of lists
        rgb_pixels_1 = img_rgb_1.tolist()
        rgb_pixels_2 = img_rgb_2.tolist()

        # Extract binary and convert to text
        extracted_binary = extract_binary_from_pixels(rgb_pixels_1, rgb_pixels_2)
        text = binary_to_text(extracted_binary)

        # Clean up memory after processing
        cleanup_images(img_rgb_1, img_rgb_2)

        del rgb_pixels_1, rgb_pixels_2
        
        return jsonify({"Final_text": text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error while processing images"}), 500


### ------------------- RUNNING FLASK APP ------------------- ###
if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import extract_binary_from_pixels 
from utils import binary_to_text

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/get", methods=["POST"])
def process_data():
    if "image1" not in request.files or "image2" not in request.form:
        return jsonify({"error": "Missing image or text"}), 400

    # Get images
    image1 = request.form["image1"]
    image2 = request.files["image2"]

    extracted_binary = extract_binary_from_pixels(image1,image2)
    text = binary_to_text(extracted_binary)

    return jsonify({
        "Final_text": text
    })



if __name__ == "__main__":
    app.run(debug=True, port=5000)
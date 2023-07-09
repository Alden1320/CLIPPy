# Import Dependencies
import torch
import clip
from PIL import Image
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pyngrok import ngrok, conf
import requests
from io import BytesIO
import os

# Set the ngrok auth token
conf.get_default().auth_token = "2RmjersP4fVZY1RxLU7wc59HgIM_2tmL6nnmEuYqeh1YK58Up"

# Start APP
app = Flask(__name__, static_folder='/content')

# Enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Declare App Functions
@app.route('/analyze', methods=['POST'])
def analyze_image():
    values = request.form.get('values')
    image_url = request.form.get('image-url')
    image_file = request.files.get('image-file')

    # Load the image
    if image_url:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    elif image_file:
        image = Image.open(BytesIO(image_file.read()))
    else:
        return jsonify({'error': 'No image provided'}), 400

    # Preprocess the image
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Encode the text
    values_list = values.split(',')
    text_input = clip.tokenize(values_list).to(device)

    # Compute the similarity between the image and text
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_input)
        similarity = (image_features @ text_features.T).softmax(dim=-1).cpu().numpy()

    # Return the results
    results = {value: float(sim) for value, sim in zip(values_list, similarity[0])}
    return jsonify(results)

@app.route('/')
def serve_html():
    return send_from_directory(app.static_folder, 'index.html')

# Run the server with ngrok
if __name__ == '__main__':
    # Specify the hostname for the static URL
    try:
        public_url = ngrok.connect(5000, hostname="e6a79a81d316-5385089081761871452.ngrok-free.app")
        print(f'Public URL: {public_url}')
    except Exception as e:
        print(f'Error: {e}')
        public_url = ngrok.connect(5000)
        print(f'Fallback to Public URL: {public_url}')
    app.run(port=5000)

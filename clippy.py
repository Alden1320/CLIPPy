# Importar las bibliotecas necesarias
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import requests
from io import BytesIO
import torch
import clip
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
import numpy as np


# Set Static Folder
app = Flask(__name__, static_folder='content')

# Determinar si se debe usar la GPU o la CPU para el modelo
device = "cuda" if torch.cuda.is_available() else "cpu"

# Cargar el modelo CLIP y el proceso de preprocesamiento
model, preprocess = clip.load("ViT-B/32", device=device)

# Definir la ruta de análisis que acepta solicitudes POST
@app.route('/')
def root():
	return send_from_directory(app.static_folder,'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Obtener los datos JSON de la solicitud
    data = request.get_json()

    # Si se proporciona una URL de imagen, descargar la imagen de la URL
    if 'imgurl' in data and data['imgurl']:
        response = requests.get(data['imgurl'])
        img = Image.open(BytesIO(response.content))
    # Si se carga un archivo de imagen, usar ese archivo
    elif 'imgfile' in data and data['imgfile']:
        img = Image.open(request.files['imgfile'])
    # Si no se proporciona ninguna imagen, devolver un error
    else:
        return jsonify({'error': 'No image provided'}), 400

    # Dividir los términos proporcionados por comas para generar las entradas de texto
    values = data['values'].split(',')

    # Preprocesar la imagen y convertirla en una entrada para el modelo CLIP
    image_input = preprocess(img).unsqueeze(0).to(device)

    # Convertir los términos en entradas de texto para el modelo CLIP
    text_input = clip.tokenize(values).to(device)

    # Calcular las características de la imagen y del texto
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_input)
        similarity = (image_features @ text_features.T).softmax(dim=-1).cpu().numpy()

    # Return the results
    results = {value: float(sim) for value, sim in zip(values, similarity[0])}

    # Devo1ver los resultados como un objeto JSON
    return jsonify(results)

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0')

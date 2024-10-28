import io
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask_cors import CORS

# Assuming you have the model loaded and class names ready
class CustomScaleLayer(tf.keras.layers.Layer):
    def __init__(self, scale_factor=1.0, **kwargs):
        super(CustomScaleLayer, self).__init__(**kwargs)
        self.scale_factor = scale_factor

    def call(self, inputs):
        return inputs * self.scale_factor

    def get_config(self):
        config = super(CustomScaleLayer, self).get_config()
        config.update({'scale_factor': self.scale_factor})
        return config

# Load your model and class names
model = load_model('final_model.h5', custom_objects={'CustomScaleLayer': CustomScaleLayer})
class_names = ['Atopic Dermatitis', 'Contact Dermatitis', 'Dyshidrotic Eczema', 'Nummular Dermatitis', 'Seborrheic Dermatitis', 'Stasis Dermatitis']

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        img = img.resize((224, 224))  # Resize to match the model input size
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Rescale
        
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions, axis=1)[0]  # Get the index of the highest probability
        predicted_class_name = class_names[predicted_class]
        
        response = {'predicted_class': predicted_class_name}
        print(response)  # Log the response
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

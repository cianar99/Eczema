import React, { useState } from 'react';
import './ImageUpload.css';

const ImageUpload = () => {
    const [result, setResult] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const fileInput = document.getElementById('fileInput');
        if (fileInput.files.length > 0) {
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);

            try {
                const response = await fetch('http://127.0.0.1:5000/predict', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }

                const result = await response.json();
                console.log(result);  // Log the result
                setResult('Predicted Class: ' + result.predicted_class);
            } catch (error) {
                console.error('Error:', error);
                setResult('Error: ' + error.message);
            }
        } else {
            setResult('Please select a file.');
        }
    };

    return (
        <div>
            <div>
            <div className="navbar">
                <h1>Eczema Detector</h1>
            </div>
            </div>
           
        <div className="background">
            <div className="glassmorphism-container">
                <h1>Upload an Image for Prediction</h1>
                <form id="uploadForm" onSubmit={handleSubmit} encType="multipart/form-data">
                    <input type="file" id="fileInput" name="file" accept="image/*" />
                    <button type="submit">Upload</button>
                </form>
                <p>{result}</p>
            </div>
        </div>
        </div>
    );
};

export default ImageUpload;
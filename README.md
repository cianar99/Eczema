
---

# Eczema Detection and Classification Using Deep Learning

## Project Overview

This project involves training a deep learning model to detect and classify different types of eczema using TensorFlow. The model is based on the InceptionResNetV2 architecture and includes a custom layer for scaling inputs. The final model is integrated into a Flask backend for predictions, which can be accessed via a React frontend.

## File Structure

```
.
├── backend/
│   ├── app.py                # Flask backend for serving predictions
│   ├── final_model.h5        # Pre-trained deep learning model (not included)
│   ├── training.ipynb        # Jupyter notebook for training the model
│   ├── test/                 # Folder containing the eczema dataset
│   │   ├── Atopic Dermatitis/
│   │   ├── Contact Dermatitis/
│   │   ├── Dyshidrotic Eczema/
│   │   ├── Nummular Dermatitis/
│   │   ├── Seborrheic Dermatitis/
│   │   └── Stasis Dermatitis/
└── frontend/
    ├── public/               # React frontend public assets
    ├── src/                  # React frontend source code
    ├── package.json          # Node.js dependencies for React
    └── README.md             # Instructions for setting up the frontend
```

## Prerequisites

Ensure you have the following software installed:

- **Python** 3.x (3.8 or 3.9)
- **TensorFlow** 2.x (for GPU support)
- **Node.js** and **npm** for frontend development
- **Flask** for the backend
- **Pillow** for image processing
- **NumPy** for numerical operations
- **Scikit-Learn** for data manipulation

## Step-by-Step Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/eczema-detection.git
cd eczema-detection
```

### 2. Backend Setup

#### Install Python Dependencies

Ensure you have a Python 3.x environment with TensorFlow version 2.x for GPU support. Install the required Python packages:

```bash
pip install tensorflow==2.9.1 flask pillow numpy scikit-learn matplotlib
```

#### Prepare the Dataset

Download the eczema dataset from [Kaggle](https://www.kaggle.com/datasets/seyamalam/eczema) and extract it into the `backend/test/` directory.

#### Train the Model

Run the `training.ipynb` notebook to train the model. This notebook will preprocess the images, train the model, and save it as `final_model.h5`.

**Note:** The `final_model.h5` is not included in the repository. You will need to train the model yourself using the provided notebook.

#### Run the Flask Backend

After training, you can start the Flask backend using the following command:

```bash
cd backend
python app.py
```

The server will start on `http://0.0.0.0:5000`. You can send POST requests to `/predict` with image files for predictions.

### 3. Frontend Setup

#### Install Node.js Dependencies

Navigate to the `frontend` directory and install the required Node.js packages:

```bash
cd ../frontend
npm install
```

#### Run the React Frontend

After installing the dependencies, you can start the React frontend by running:

```bash
npm start
```

This will start the development server on `http://localhost:3000`, which will interact with the Flask backend for predictions.

## Using the Application

1. **Start the Flask Backend**:
   ```bash
   cd backend
   python app.py
   ```
   
2. **Start the React Frontend**:
   ```bash
   cd ../frontend
   npm start
   ```

3. **Interact with the Application**:
   Open your web browser and navigate to `http://localhost:3000` to use the frontend, which will send images to the Flask backend for eczema detection.


## Troubleshooting

### Custom Layer Error

If you encounter an error related to the custom layer `CustomScaleLayer`, ensure that:

- The class is defined in the `app.py` file.
- The `load_model` function in `app.py` includes `custom_objects={'CustomScaleLayer': CustomScaleLayer}`.

### TensorFlow GPU Support

This project uses TensorFlow version 2.x for GPU support. Ensure you have the correct version installed by running:

```bash
pip install tensorflow-gpu==2.x
```

### Model Not Included

The pretrained model (`final_model.h5`) is not included in the repository. You need to train the model using the provided notebook before running the backend.

## Conclusion

This project provides a full-stack solution for detecting and classifying eczema using a deep learning model, Flask for backend API, and React for frontend UI. Follow the setup instructions to train the model and deploy the application.

--- 

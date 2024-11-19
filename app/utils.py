from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import os

# Function to load the heart disease prediction model
def model_load():
    base_path = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_path, '..', 'model_training', 'model.keras')
    return load_model(model_path)

# Function to preprocess the input data before prediction
def preprocess_input(data):
    # Convert input data to the appropriate format (array of floats)
    processed_data = [
        float(data["Age"]),
        float(data["Sex"]),
        float(data["ChestPainType"]),
        float(data["RestingBP"]),
        float(data["Cholesterol"]),
        float(data["FastingBS"]),
        float(data["RestingECG"]),
        float(data["MaxHR"]),
        float(data["ExerciseAngina"]),
        float(data["Oldpeak"]),
        float(data["ST_Slope"]),
    ]
    return np.array(processed_data)

# services.py

import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from .utils import model_load, preprocess_input

# Load the pre-trained model
model = model_load()

# Load saved training data for SHAP explainer
X_train = pd.read_csv('data/X_train.csv')

# Initialize SHAP explainer
explainer = shap.KernelExplainer(model.predict, X_train.iloc[:100, :])

def make_prediction(data):
    """
    Preprocess input, make prediction, and compute SHAP values.
    """
    # Preprocess the data
    input_data = preprocess_input(data)

    # Reshape input_data to be 2D (1 sample, n features)
    input_data = input_data.reshape(1, -1)

    # Make prediction using the model
    output = model.predict(input_data)
    result = float(output[0][0])

    # Compute SHAP values
    shap_values = explainer.shap_values(input_data)

    # Reshape shap_values to (1, n features)
    shap_values = shap_values.reshape(1, -1)

    return result, shap_values, input_data


def generate_shap_plot(shap_values, input_data, feature_names):
    """
    Generate SHAP plot as a base64 encoded string.
    """
    plt.switch_backend("Agg")
    plt.figure()

    # Plot SHAP summary
    shap.summary_plot(shap_values, input_data, feature_names=feature_names, show=False)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)  # Move the cursor to the start of the stream
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return plot_url

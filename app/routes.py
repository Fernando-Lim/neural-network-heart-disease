# routes.py

from flask import Blueprint, render_template, request, jsonify
from .services import make_prediction, generate_shap_plot

# Create a Blueprint for routes
main = Blueprint('main', __name__)

# Route 1: Welcome/Homepage Route
@main.route("/", methods=["GET"])
def home():
    return render_template("home.html")  # Render a welcome/introduction page


# Route 2: Data Input Route
@main.route("/input", methods=["GET", "POST"])
def input_data():
    if request.method == "GET":
        return render_template("input_data.html")  # Render the data input form

    if request.method == "POST":
        # Collect patient data from the form
        data = {
            "Age": request.form["age"],
            "Sex": request.form["sex"],
            "ChestPainType": request.form["cp"],
            "RestingBP": request.form["trestbps"],
            "Cholesterol": request.form["chol"],
            "FastingBS": request.form["fbs"],
            "RestingECG": request.form["restecg"],
            "MaxHR": request.form["maxhr"],
            "ExerciseAngina": request.form["exang"],
            "Oldpeak": request.form["oldpeak"],
            "ST_Slope": request.form["slope"]
        }

        # Call the service to make prediction and get SHAP values
        result, shap_values, input_data = make_prediction(data)

        # Define the feature names for the SHAP plot
        feature_names = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

        # Generate the SHAP plot
        plot_url = generate_shap_plot(shap_values, input_data, feature_names)

        # Render the result page with the prediction and SHAP explanation
        return render_template("result.html", result=result, shap_plot=plot_url)


# Route 3: Result/Explanation Route
@main.route("/result", methods=["GET"])
def result_page():
    # Get the prediction result and SHAP explanation
    result = request.args.get('result', type=float)
    plot_url = request.args.get('shap_plot', default=None)

    # Render the result page with SHAP plot
    return render_template("result.html", result=result, shap_plot=plot_url)

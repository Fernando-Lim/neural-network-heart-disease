# Heart Disease Risk Prediction  

This project is a web-based application for predicting heart disease risk using a neural network model. The application provides predictions based on clinical data and includes a feature visualization using SHAP (SHapley Additive exPlanations) to explain the factors contributing to the risk score.  

## Dataset  

The dataset used for this project is the **Heart Failure Prediction Dataset** from Kaggle ([link](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)). The data originates from the UCI Machine Learning Repository ([link](https://archive.ics.uci.edu/dataset/45/heart+disease)) and includes clinical parameters such as age, cholesterol levels, blood pressure, and other relevant features.  

## Setup Instructions  

To set up and run the Flask project, follow these steps:  

1. **Clone the Repository**  
   ```
   git clone <repository_url>  
   cd <repository_folder>  
   ```  

2. **Install Required Libraries**  
   Ensure you have Python 3.8 or higher installed. Then, install the required Python packages:  
   ```
   pip install -r requirements.txt  
   ```  

   The `requirements.txt` file contains the following dependencies:  
   ```  
   Flask==3.0.3  
   matplotlib==3.7.2  
   numpy==1.25.2  
   pandas==2.0.0  
   shap==0.46.0  
   tensorflow==2.16.2  
   ```  

3. **Run the Flask Application**  
   Start the Flask server:  
   ``` 
   flask run
   ```  
   By default, the application will be available at `http://127.0.0.1:5000`.  

4. **Features**  
   - **Heart Disease Risk Prediction**: Enter clinical parameters to get a risk prediction (e.g., age, blood pressure, cholesterol levels).  
   - **SHAP Visualization**: View a detailed explanation of how each parameter influences the prediction outcome.  

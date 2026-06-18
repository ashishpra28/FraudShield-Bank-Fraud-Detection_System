# Import libraries 
import joblib
import pandas as pd

# Load model 
model = joblib.load("artifacts/model.pkl")

# Define model version 
MODEL_VERSION = '1.0.0'

# Create predict output function 
def predict_output(user_input:dict):

    input_df = pd.DataFrame([user_input])

    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    return prediction, probability
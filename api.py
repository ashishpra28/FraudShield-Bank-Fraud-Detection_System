# Import libraries 
from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from src.predict import model, predict_output,MODEL_VERSION


# Define fastapi object 
app = FastAPI()


# Create home endpoint 
@app.get('/')
def home():
    return {
        "message": "Welcome to Bank Fraud Detection API",
        "status": "Running",
        "description":"This API predicts whether a bank transaction is fraudulent or legitimate.",
        "model": "XGBoost",
        "docs": "/docs",
        "predict_endpoint": "/predict",
        "health_check_endpoint":"/health"
    }

# Create health check endpoint 
@app.get('/health')
def health_check():
    return {
        "status":"OK",
        "version":MODEL_VERSION,
        "model_loaded":model is not None
    }

# Create predic endpoint 
@app.post('/predict')
def predict_fraud(data: UserInput):
    
    user_input = {
        'hour': data.hour,
        'type': data.type,
        'amount':data.amount,
        'balanceDiffOrig': data.balanceDiffOrig,
        'balanceDiffDest': data.balanceDiffDest
    }

    try:
        prediction, probability  = predict_output(user_input)

        return {
            'prediction':prediction,
            'fraud_probability':round(probability,4)
            }
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


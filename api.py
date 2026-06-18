# Import libraries 
from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated 
import joblib
import pandas as pd

# Import model 
model = joblib.load("artifacts/model.pkl")

# Define fastapi object 
app = FastAPI()

# Create pydantic model to validate input data 
class UserInput(BaseModel): 
    
    hour: Annotated[int,Field(...,ge=0,le=23,description="Transaction hour (0-23)")]

    type:Annotated[Literal['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'],Field(...,description="Type of the transaction")]

    amount:Annotated[float,Field(...,ge=0,description="Type of the transaction")]

    oldbalanceOrg:Annotated[float,Field(...,ge=0,description="Old balance of the sender")]

    newbalanceOrig:Annotated[float,Field(...,ge=0,description="New balance of the sender")]
    
    oldbalanceDest:Annotated[float,Field(...,ge=0,description="Old balance of the receiver")]

    newbalanceDest:Annotated[float,Field(...,ge=0,description="New balance of the receiver")]

    # Create new features - Feature Engineering
    @computed_field
    @property 
    def balanceDiffOrig(self)->float:
        return self.oldbalanceOrg - self.newbalanceOrig 
    
    @computed_field 
    @property 
    def balanceDiffDest(self)->float: 
        return self.newbalanceDest - self.oldbalanceDest

# Create predic endpoint 
@app.post('/predict')
def predict_fraud(data: UserInput):
    
    input_df = pd.DataFrame([{
        'hour': data.hour,
        'type': data.type,
        'amount':data.amount,
        'balanceDiffOrig': data.balanceDiffOrig,
        'balanceDiffDest': data.balanceDiffDest
    }])

    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    return {
        'prediction':prediction,
        'fraud_probability':round(probability,4)
        }


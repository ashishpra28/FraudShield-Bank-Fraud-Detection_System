# Import libraries 
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated 


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
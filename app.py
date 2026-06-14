from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field , computed_field
from typing import Literal,Annotated
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")


app = FastAPI()

class UserInput(BaseModel):
    education: Annotated[Literal["Graduate", "Not Graduate"],Field(..., description='Grauated or Not Graduated')]
    self_employed: Annotated[Literal['Yes','No'],Field(..., description='Yes or No')]
    income_annum: Annotated[int , Field(...,gt=0,description ='Annum income ')]
    loan_amount:  Annotated[int , Field(...,gt=0,description ='Amount of loan')]
    loan_term:  Annotated[int , Field(...,gt=0,description ='term of loan')]
    cibil_score:  Annotated[int , Field(...,ge=300,le=900,description ='cibil Score')]
    residential_assets_value:  Annotated[int , Field(...,ge=0, description ='value of the residential assets')]
    commercial_assets_value:  Annotated[int , Field(...,ge=0, description ='Value of commercial assets ')]
    luxury_assets_value:  Annotated[int , Field(..., ge=0,description ='Value of luxury assets value')]
    bank_asset_value:  Annotated[int , Field(..., ge=0,description ='Value of bank assert')]


@app.post("/predict")
def predict_loan_approval(data : UserInput):
    input_df =pd.DataFrame([{
        'education' : data.education,
        'self_employed':data.self_employed,
        'income_annum':data.income_annum,
        'loan_amount':data.loan_amount,
        'loan_term':data.loan_term,
        'cibil_score':data.cibil_score,
        'residential_assets_value':data.residential_assets_value,
        'commercial_assets_value':data.commercial_assets_value,
        'luxury_assets_value':data.luxury_assets_value,
        'bank_asset_value':data.bank_asset_value
    }])

    prediction = model.predict(input_df)[0]
    result = "Approved" if prediction == 0 else "Rejected"

    return JSONResponse(status_code = 200,content ={'prediction_category':result})

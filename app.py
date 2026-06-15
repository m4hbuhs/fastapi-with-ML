from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output,model,MODEL_VERSION
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {'message':'loan approval prediction Api'}

@app.get('/health')
def health_check():
    return {'status':'OK',
            'version': MODEL_VERSION,
            'model_loaded': model is not None
            
            }

@app.post("/predict",response_model = PredictionResponse)
def predict_loan_approval(data : UserInput):
    user_input ={
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
    }
    try:
        prediction =predict_output(user_input)

        return JSONResponse(status_code = 200,content ={'prediction_category':prediction})
    except Exception as e:
        return JSONResponse(status_code =200,content = str(e))
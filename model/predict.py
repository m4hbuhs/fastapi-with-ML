import joblib
import pandas as pd
model = joblib.load("model/loan_model.pkl")

#MLFLOW
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]

    result = "Approved" if prediction == 0 else "Rejected"

    confidence = float(max(probabilities))

    return {
        "prediction_category": result,
        "confidence": round(confidence, 4),
        "approved_probability": round(float(probabilities[0]), 4),
        "rejected_probability": round(float(probabilities[1]), 4)
    }
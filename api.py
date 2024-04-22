from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
from schemas import HeartData

app = FastAPI(
    title="Apis Predict Heart Attack",
    version="0.0.1"
)

# LOAD MODEL
model = joblib.load("model/logistic_regression_model_v01.pkl")

@app.post("/api/v1/predict-heart-attack", tags=["predict-heart-attack"])
async def predict(data: HeartData):
    try:
        df = pd.DataFrame(data.dict(), index=[0])
        prediction = model.predict(df)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=prediction[0]
        )
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )

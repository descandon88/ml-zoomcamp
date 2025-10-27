import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import requests


class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

with open("pipeline_v1.bin", "rb") as f_in:
    model = pickle.load(f_in)

app = FastAPI()

@app.post("/predict")
def predict(client: Client):
    X = [client.dict()]
    prediction = model.predict_proba(X)[0, 1]
    return {"subscription_probability": prediction}



url = "http://127.0.0.1:8000/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client).json()
print(response)

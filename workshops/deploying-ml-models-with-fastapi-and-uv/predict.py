#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import sklearn

from typing import Dict, Any
from typing import Literal

import pickle

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import make_pipeline 
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field



customer = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'yes',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 6,
    'monthlycharges': 29.85,
    'totalcharges': 129.85
}

#Request

class Customer(BaseModel):
    pass




class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool

#Response
app = FastAPI(title="churn-prediction")


with open('model.bin','rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer): 
    result = pipeline.predict_proba(customer)[0,1]
    return float(result)

@app.post("/predict")

# def predict(customer:Customer) -> PredictResponse :
def predict(customer: Dict[str, Any]):
    prob = predict_single(customer)

    return {
        "churn_probability": prob,
        "churn" : bool(prob >= 0.5)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

#churn = pipeline.predict_proba(customer)[0,1]

#print('prob of churning', churn)

#if churn >=0.5:
#    print('send email with promo')
#else:
#    print('dont do anything')






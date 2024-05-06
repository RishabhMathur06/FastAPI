import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from BankNotes import BankNote

app = FastAPI()

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# index route
@app.get('/')
def index():
    return {'message': 'Hello, world'}

# Route with single parameter
@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Hello, {name}'}

# Expose the prediction functionality, make a prediction from the passed,
#    JSON data and return the predicted Bank Note with the confidence.
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    if(prediction[0] > 0.5):
        prediction = "Fake Note"
    else:
        prediction = "It's a bank note"
    return{
        'prediction' : prediction
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


from fastapi import FastAPI
from pydantic import BaseModel, confloat
import joblib
import numpy as np


model = joblib.load("iris_model.joblib")

app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: confloat(gt=0)
    sepal_width: confloat(gt=0)
    petal_length: confloat(gt=0)
    petal_width: confloat(gt=0)

@app.post("/predict")
def predict(features: IrisFeatures):
    data = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])
    prediction = model.predict(data)
    species = ["setosa", "versicolor", "virginica"]
    predicted_species = species[prediction[0]]
    return {"predicted_species": predicted_species}

#go to terminal and change directory to where main.py is located then run the venv using venv\Scripts\activate
# To run the FastAPI app, use the command:
# uvicorn main:app --reload
#then head to the link/docs to see the API documentation and test the endpoint
# The model can be tested by sending a POST request to /predict with the required features.
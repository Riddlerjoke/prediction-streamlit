# Description: Fichier principal de l'API
from fastapi import FastAPI, File, UploadFile, HTTPException
import numpy as np

import pickle
import pandas as pd

import mlflow
import os
import boto3

from models import Credit, Credit2
from tag import tags
from description import descriptions



# Création de l'application
app = FastAPI(
       title="API de prediction",
       description=descriptions,
       version="1.0.0",
       openapi_tags=tags,
       terms_of_service="https://example.com/terms/",
       contact={
            "name": "Jay Wayne Fairey",
            "url": "https://x-force.example.com/contact/",
            "email": "dp@x-force.example.com",
       },
       license_info={
            "name": "Apache 2.0",
            "identifier": "MIT",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
       },
)


# Chargement du modèle
model1 = pickle.load(open('utils/model_1.pkl', 'rb'))

# Chargement du modèle 2
model2 = pickle.load(open('utils/model_2.pkl', 'rb'))


# Endpoint sans paramètre
@app.get("/", tags=["Hello"])
def read_root():
    return {"message": "Hello World"}


# Endpoint avec paramètre
@app.get("/hello", tags=["Hello"])
def hello(name: str = 'World'):
    return {"message": f"Hello {name}"}


####################################################################################################################
# Section prediction (model) : CRUD sur les models
####################################################################################################################

@app.post("/predict/", tags=["PredictV1"])
def predict(credit: Credit):
    data = dict(credit)  # Convertir l'objet Pydantic en dictionnaire
    data = {
        'Gender': data['Gender'],
        'Age': data['Age'],
        'Physical Activity Level': data['PhysicalActivityLevel'],
        'Heart Rate': data['HeartRate'],
        'Daily Steps': data['DailySteps'],
        'BloodPressure_high': data['BloodPressure_high'],
        'BloodPressure_low': data['BloodPressure_low'],
    }
    data_df = pd.DataFrame([data])  # Convertir le dictionnaire en DataFrame
    prediction1 = model1.predict(data_df)

    # Convertir le résultat de la prédiction en un type Python natif
    prediction1 = prediction1[0].item()

    # Sauvegarder la prédiction dans un fichier
    with open('result/predictions-model1.txt', 'a') as f:
        f.write(str(prediction1) + '\n')

    return {"prediction": prediction1}


@app.post("/predict2/", tags=["PredictV2"])
def predict2(credit: Credit2):
    data2 = dict(credit)
    data = {
        'Physical Activity Level': data2['PhysicalActivityLevel'],
        'Heart Rate': data2['HeartRate'],
        'Daily Steps': data2['DailySteps'],

    }
    data_df = pd.DataFrame([data])  # Convertir le dictionnaire en DataFrame
    prediction2 = model2.predict(data_df)

    # Convertir le résultat de la prédiction en un type Python natif
    prediction2 = prediction2[0].item()

    # Sauvegarder la prédiction dans un fichier
    with open('result/predictions-model2.txt', 'a') as f:
        f.write(str(prediction2) + '\n')

    return {"prediction": prediction2}


@app.get("/result/")
def get_prediction1():
    with open('result/predictions-model1.txt', 'r') as f:
        return f.read()


@app.get("/result2/")
def get_prediction2():
    with open('result/predictions-model2.txt', 'r') as f:
        return f.read()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f"result/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename}


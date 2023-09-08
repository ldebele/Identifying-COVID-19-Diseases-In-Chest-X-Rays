import os
import glob
import numpy as np
import tensorflow as tf

import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel




app = FastAPI(title="Identify COVID-19 Disease In Chest X-Rays")


class FileUpload(BaseModel):
    file: UploadFile


class PredictedResponse(BaseModel):
    disease_type: str



@app.on_event("startup")
def load_model():
    # Load the model
    global model
    model_path = glob.glob('../models/*.h5')[0]
    model = tf.tf.keras.models.load_model(model_path)


@app.get("/")
def home():
    return {"message": "This is your home page"}


@app.post("/predict")
async def prediction(file: FileUpload):
    # check the uploaded file
    if file.content_type.startswith("image/"):
        img = await file.read() 
        pred = model.predict(img)
        pred = model.predict()
        pred = np.round(pred)
        return {"Disease Type": str(pred)}
    else:
        return {"error": "Uploaded file is not an image"}


if __name__ == "__main__"
    uvicorn.run(app, host="0.0.0.0", port=8080)
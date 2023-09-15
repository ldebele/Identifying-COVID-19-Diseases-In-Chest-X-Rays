import numpy as np
from PIL import Image

import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import tensorflow as tf
from tensorflow.keras.preprocessing import image 
from tensorflow.keras.applications.inception_v3 import preprocess_input 



app = FastAPI(title="Identify COVID-19 Disease In Chest X-Rays")

class FileUpload(BaseModel):
    file: UploadFile


@app.on_event("startup")
def load_model():
    # Load the model
    global model
    model_path = "./models/2023-09-02_xception.h5"
    model = tf.keras.models.load_model(model_path)


# redirect
@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")


@app.get("/home")
def home():
    return {"message": "This is your home page"}


@app.post("/predict")
def predict(file: UploadFile = File(...)):

    # Check if the uploaded file
    fileExtension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

    # Read and preprocess the uploaded image
    img = Image.open(file.file)
    img = img.resize((224, 224))
    img = img.convert("RGB")
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # predict the image
    predict_coef = model.predict(img)
    disease_type = "COVID" if predict_coef >= 0.25 else "Non-COVID"

    return {"Disease Type": disease_type}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os


app = FastAPI(title="API de predicción de precios - Datathon mini")

# 🔓 Permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "modelo.pkl")
model = None


# Esquema de entrada con validación básica
class PisoInput(BaseModel):
    metros: float = Field(..., gt=0, description="Metros cuadrados")
    habitaciones: int = Field(..., ge=0, description="Número de habitaciones")
    baños: int = Field(..., ge=0, description="Número de baños")
    balcones: int = Field(..., ge=0, description="Número de balcones")


@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {"mensaje": "API de predicción de precios"}


@app.post("/predict")
def predict(input: PisoInput):
# Construimos array 2D para el modelo
    X = np.array([[input.metros, input.habitaciones, input.baños, input.balcones]])
    pred = model.predict(X)[0]
    return {"precio_estimado": float(pred)}
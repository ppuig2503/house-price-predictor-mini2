import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os


DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "house_prices.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "modelo.pkl")


# Cargar datos
df = pd.read_csv(DATA_PATH)


# Características y objetivo
X = df[["metros", "habitaciones", "baños", "balcones"]]
y = df["precio"]


# Entrenar modelo simple
model = LinearRegression()
model.fit(X, y)


# Guardar
joblib.dump(model, MODEL_PATH)
print(f"Modelo entrenado y guardado en {MODEL_PATH}")


# Opcional: mostrar métricas sencillas
from sklearn.metrics import mean_squared_error
preds = model.predict(X)
rmse = mean_squared_error(y, preds, squared=False)
print(f"RMSE sobre entrenamiento: {rmse:.2f}")
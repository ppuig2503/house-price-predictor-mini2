import sys
import os

try:
	import pandas as pd
	import numpy as np
	from sklearn.linear_model import LinearRegression
	import joblib
except Exception as e:
	# Provide a helpful message if dependencies are missing or incompatible
	print("Error importing required packages:", repr(e))
	print()
	print("Please create and activate a virtual environment and install required packages:")
	print(r"python -m venv venv")
	print(r"venv\Scripts\activate")
	print(r"pip install --upgrade pip")
	print(r"pip install pandas scikit-learn joblib numpy")
	sys.exit(1)


DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "house_prices.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "modelo.pkl")


# Cargar datos
if not os.path.exists(DATA_PATH):
	print(f"Data file not found: {DATA_PATH}")
	sys.exit(1)

df = pd.read_csv(DATA_PATH)


# Características y objetivo
required_cols = ["metros", "habitaciones", "baños", "balcones", "precio"]
missing = [c for c in required_cols if c not in df.columns]
if missing:
	print("CSV is missing required columns:", missing)
	print("Available columns:", list(df.columns))
	print("First rows of the file:")
	print(df.head().to_string())
	sys.exit(1)

X = df[["metros", "habitaciones", "baños", "balcones"]]
y = df["precio"]


# Entrenar modelo simple
model = LinearRegression()
model.fit(X, y)


# Guardar
joblib.dump(model, MODEL_PATH)
print(f"Modelo entrenado y guardado en {MODEL_PATH}")


# Opcional: mostrar métricas sencillas
preds = model.predict(X)
# Compute RMSE in a way that's compatible across sklearn versions
try:
	from sklearn.metrics import mean_squared_error
	# prefer squared=False when available
	try:
		rmse = mean_squared_error(y, preds, squared=False)
	except TypeError:
		# older/newer signatures: compute sqrt of MSE
		rmse = np.sqrt(mean_squared_error(y, preds))
except Exception:
	# If sklearn.metrics isn't available for some reason, fallback to numpy
	rmse = np.sqrt(np.mean((y - preds) ** 2))

print(f"RMSE sobre entrenamiento: {rmse:.2f}")
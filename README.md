# 🏠 Datathon Mini - React + FastAPI + ML

Mini proyecto para practicar antes del Datathon.  
Incluye:

- **Backend (FastAPI)**: expone un endpoint `/predict` para estimar el precio de un piso.
- **Machine Learning Core (scikit-learn)**: modelo lineal simple entrenado con datos sintéticos.
- **Frontend (React)**: formulario que permite al usuario introducir datos y ver la predicción.

---

## ⚙️ Requisitos

- Python **3.8 o superior**
- Node.js **16 o superior** (recomendado por `create-react-app`)

---

## 🚀 Backend

### 1️⃣ Ir a la carpeta del backend
```bash
cd backend

### 2️⃣ Crear un entorno virtual e instalar dependencias
En Windows (CMD o PowerShell):

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

En Mac / Linux:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3️⃣ Entrenar y guardar el modelo
python train_model.py

Esto generará un archivo modelo.pkl dentro de la carpeta backend
y mostrará una métrica de error (RMSE) sobre el conjunto de entrenamiento.

### 4️⃣ Ejecutar la API
uvicorn main:app --reload

La API estará disponible en:
👉 http://127.0.0.1:8000

Puedes probarla con:

Swagger UI: http://127.0.0.1:8000/docs

Ejemplo POST (en Swagger):

{
  "metros": 80,
  "habitaciones": 3,
  "baños": 1,
  "balcones": 1
}

###########################################################

🧩 Frontend (React)
1️⃣ Ir a la carpeta del frontend
cd frontend

2️⃣ Instalar dependencias
npm install

3️⃣ Ejecutar el servidor de desarrollo
npm start


El frontend se abrirá en 👉 http://localhost:3000

🧠 Uso

Abre el navegador en http://localhost:3000

Rellena los campos del formulario (metros, habitaciones, baños, balcones)

Pulsa “Predecir precio”

Verás el precio estimado calculado por el modelo de ML a través del backend FastAPI.

### ESTRUCTURA DE CARPETAS DEL PROYECTO

datathon-mini/
├── backend/
│   ├── data/
│   │   └── house_prices.csv
│   ├── main.py
│   ├── train_model.py
│   ├── modelo.pkl
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.js
    │   └── index.js
    ├── public/
    │   └── index.html
    └── package.json


✅ Siguientes pasos

Entrena el modelo (python train_model.py)

Arranca el backend (uvicorn main:app --reload)

Lanza el frontend (npm start)

Comprueba que el formulario envía los datos correctamente y devuelve un precio.
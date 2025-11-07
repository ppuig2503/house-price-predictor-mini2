import React, { useState } from "react";

function App() {
  const [metros, setMetros] = useState(80);
  const [habitaciones, setHabitaciones] = useState(3);
  const [baños, setBanos] = useState(1);
  const [balcones, setBalcones] = useState(1);
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResultado(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          metros: Number(metros),
          habitaciones: Number(habitaciones),
          baños: Number(baños),
          balcones: Number(balcones),
        }),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Error en la petición: ${res.status} - ${text}`);
      }

      const data = await res.json();
      setResultado(data.precio_estimado);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: 600,
        margin: "40px auto",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1>Predicción de precio (mini)</h1>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: 8 }}>
          <label>Metros: </label>
          <input
            type="number"
            value={metros}
            onChange={(e) => setMetros(e.target.value)}
          />
        </div>
        <div style={{ marginBottom: 8 }}>
          <label>Habitaciones: </label>
          <input
            type="number"
            value={habitaciones}
            onChange={(e) => setHabitaciones(e.target.value)}
          />
        </div>
        <div style={{ marginBottom: 8 }}>
          <label>Baños: </label>
          <input
            type="number"
            value={baños}
            onChange={(e) => setBanos(e.target.value)}
          />
        </div>
        <div style={{ marginBottom: 8 }}>
          <label>Balcones: </label>
          <input
            type="number"
            value={balcones}
            onChange={(e) => setBalcones(e.target.value)}
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Prediciendo..." : "Predecir precio"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {resultado !== null && (
        <div style={{ marginTop: 20 }}>
          <h2>Precio estimado: {resultado.toLocaleString()} €</h2>
        </div>
      )}
    </div>
  );
}

export default App;

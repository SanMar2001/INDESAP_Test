import { useState } from "react";
import Timer from "./components/Timer";
import { endSession, startSession } from "./services/api";

export default function App() {
  const [code, setCode] = useState("");
  const [active, setActive] = useState(false);
  const [startTime, setStartTime] = useState(null);
  const [totalTime, setTotalTime] = useState(null);
  const [message, setMessage] = useState(null);

  const handleStart = async () => {
    if (!code.trim()) {
      setMessage("Debe ingresar un código");
      return;
    }

    try {
      const data = await startSession(code);

      setActive(true);
      setStartTime(new Date());
      setMessage(data.message);
      setTotalTime(null);
    } catch (err) {
      setMessage("Error al iniciar sesión");
    }
  };

  const handleEnd = async () => {
    if (!code.trim()) {
      setMessage("Debe ingresar un código");
      return;
    }

    try {
      const data = await endSession(code);

      setActive(false);
      setMessage(data.message);
      setTotalTime(data.total_time);
    } catch (err) {
      setMessage("No hay sesión activa");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "80px" }}>
      <h1>Control de Sesión</h1>

      <input
        type="text"
        placeholder="Ingrese su código"
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <div style={{ marginTop: "20px" }}>
        <button onClick={handleStart}>Iniciar sesión</button>

        <button onClick={handleEnd}>Terminar sesión</button>
      </div>

      {message && <p style={{ marginTop: "20px" }}>{message}</p>}

      {active && <Timer running={active} startTime={startTime} />}

      {totalTime && <h3>Total trabajado: {totalTime}</h3>}
    </div>
  );
}

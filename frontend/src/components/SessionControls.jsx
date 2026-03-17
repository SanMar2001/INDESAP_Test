export default function SessionControls({ onStart, onEnd, active }) {
  return (
    <div>
      {!active && <button onClick={onStart}>Iniciar sesión</button>}

      {active && <button onClick={onEnd}>Terminar sesión</button>}
    </div>
  );
}

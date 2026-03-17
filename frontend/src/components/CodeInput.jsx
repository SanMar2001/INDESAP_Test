import { useState } from "react";

export default function CodeInput({ onSubmit }) {
  const [code, setCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (code.trim()) {
      onSubmit(code);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Ingrese su código"
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <button type="submit">Ingresar</button>
    </form>
  );
}

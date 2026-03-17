import { useEffect, useState } from "react";

export default function Timer({ running, startTime }) {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    if (!running) return;

    const interval = setInterval(() => {
      const now = new Date();
      const diff = Math.floor((now - new Date(startTime)) / 1000);
      setSeconds(diff);
    }, 1000);

    return () => clearInterval(interval);
  }, [running, startTime]);

  const format = (s) => {
    const h = String(Math.floor(s / 3600)).padStart(2, "0");
    const m = String(Math.floor((s % 3600) / 60)).padStart(2, "0");
    const sec = String(s % 60).padStart(2, "0");
    return `${h}:${m}:${sec}`;
  };

  return <h2 style={{ marginTop: "30px" }}>{format(seconds)}</h2>;
}

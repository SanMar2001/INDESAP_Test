const API_URL = "http://localhost:8001/api";

export async function startSession(code) {
  const res = await fetch(`${API_URL}/start/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code }),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.detail || "Error");
  }

  return data;
}

export async function endSession(code) {
  const res = await fetch(`${API_URL}/end/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code }),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.detail || "Error");
  }

  return data;
}

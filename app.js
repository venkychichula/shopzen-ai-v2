const chat = document.querySelector("#chat");
const form = document.querySelector("#chat-form");
const input = document.querySelector("#message");
const status = document.querySelector("#status");

function addMessage(text, type) {
  const el = document.createElement("div");
  el.className = `msg ${type}`;
  el.textContent = text;
  chat.appendChild(el);
  chat.scrollTop = chat.scrollHeight;
}

addMessage(
  "Hi! I'm ShopZen AI V2. Tell me what you want to buy, your budget, and what matters most.",
  "ai"
);

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  status.textContent = "ShopZen is thinking...";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message}),
    });
    const data = await response.json();
    addMessage(data.reply || "No response received.", "ai");
    status.textContent = data.mode === "ai"
      ? "AI engine connected."
      : "V2 foundation response.";
  } catch {
    addMessage("Could not reach the ShopZen backend.", "ai");
    status.textContent = "Connection error.";
  }
});

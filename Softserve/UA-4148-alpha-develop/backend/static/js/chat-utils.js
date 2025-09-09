export function escapeHTML(str) {
  const escapes = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" };
  return str.replace(/[&<>"']/g, char => escapes[char]).replace(/\n/g, "<br>");
}

export function renderMessage(message, userId) {
  const { id, sender_id, sender_first_name, sender_last_name, text, timestamp, is_read } = message;

  const firstName = sender_first_name || "";
  const lastName = sender_last_name || "";
  const name = `${firstName} ${lastName}`.trim() || (String(sender_id) === String(userId) ? "You" : "Unknown");
  const timeStr = new Date(timestamp).toLocaleString();
  const readStatus = (String(sender_id) === String(userId)) ? `<span class="read-status">${is_read ? "✅" : "🕓"}</span>` : "";

  const div = document.createElement("div");
  div.className = "message";
  div.dataset.messageId = id;
  div.dataset.senderId = sender_id;
  div.dataset.read = is_read ? "true" : "false";

  div.innerHTML = `<strong>${escapeHTML(name)}</strong>
                   <em style="font-size:0.8em;">(${escapeHTML(timeStr)})</em>:
                   ${escapeHTML(text)} ${readStatus}`;

  return div;
}

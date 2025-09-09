import { escapeHTML, renderMessage } from './chat-utils.js';

let socket = null;

function scrollBottom(container) {
  container.scrollTo({ top: container.scrollHeight, behavior: "smooth" });
}

function cleanupChat() {
  if (socket) {
    socket.close(1000, "Cleanup");
    socket = null;
  }
}

function initChatRoom() {
  console.log("💬 initChatRoom called");
  cleanupChat();

  const chatRoot = document.getElementById("chat-root");
    if (!chatRoot) return;

  const userId = chatRoot.dataset.userId;
  const otherUserId = chatRoot.dataset.otherUserId;

  const messagesContainer = document.getElementById("messages");
  const messageForm = document.getElementById("message-form");
  const messageInput = document.getElementById("message-input");
  const goBackBtn = document.getElementById("go-back-btn");
  const logoutBtn = document.getElementById("logout-btn");

  if (!messagesContainer || !messageForm || !messageInput) return;

  goBackBtn?.addEventListener("click", () => window.location.href = "/chat/");
  logoutBtn?.addEventListener("click", () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/chat/login/";
  });

  const accessToken = localStorage.getItem("access");
  if (!accessToken) {
    alert("No access token found.");
    window.location.href = "/chat/login/";
    return;
  }

  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  socket = new WebSocket(`${protocol}://${window.location.host}/ws/chat/${otherUserId}/?token=${accessToken}`);

  let offset = parseInt(messagesContainer.dataset.offset || "0");

  socket.onopen = () => {
    console.log("🔌 WS connected");
    messagesContainer.dataset.loading = "true";
    socket.send(JSON.stringify({ type: "history", offset }));
    requestAnimationFrame(() => {
      markVisibleMessagesAsRead();
    });
    messageInput.focus();
  };

  socket.onclose = (event) => {
      console.warn("🔌 WS closed", event.code, event.reason);
      if (event.reason.includes("Invalid") || event.reason.includes("expired")) {
        alert("Session expired. Please log in again.");
        window.location.href = "/chat/login/";
        return;
      }

      if (event.code !== 1000) {
        console.warn("🔌 WS closed unexpectedly. Reconnecting in 2s");
        setTimeout(initChatRoom, 2000);
      }
  };
  socket.onerror = err => console.error("🔌 WS error", err);

  socket.onmessage = event => {
    const data = JSON.parse(event.data);

    if (data.type === "message") {
      messagesContainer.appendChild(renderMessage(data, userId));
      scrollBottom(messagesContainer);
      markVisibleMessagesAsRead();
    }

    if (data.type === "read") {
      data.message_ids.forEach(msgId => {
        const msgDiv = document.querySelector(`.message[data-message-id="${msgId}"] .read-status`);
        if (msgDiv) msgDiv.textContent = "✅";
      });
    }

    if (data.type === "history" && data.messages.length) {
      const prevHeight = messagesContainer.scrollHeight;
      const frag = document.createDocumentFragment();
      data.messages.forEach(msg => frag.appendChild(renderMessage(msg, userId)));
      messagesContainer.prepend(frag);

      offset += data.messages.length;
      messagesContainer.dataset.offset = offset;
      messagesContainer.scrollTop = messagesContainer.scrollHeight - prevHeight;
      messagesContainer.dataset.loading = "";
      requestAnimationFrame(() => {
          markVisibleMessagesAsRead();
      });
    }
  };

  messageForm.onsubmit = e => {
    e.preventDefault();
    const text = messageInput.value.trim();
    if (!text || socket.readyState !== WebSocket.OPEN) return;

    socket.send(JSON.stringify({ type:"message", message:text }));

    messageInput.value = "";
    messageInput.focus();
  };

  messageInput.onkeydown = e => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      messageForm.requestSubmit();
    }
  };

  function markVisibleMessagesAsRead() {
      const unreadEls = document.querySelectorAll(`.message[data-sender-id="${otherUserId}"]:not([data-read="true"])`);
      const unreadIds = Array.from(unreadEls).map(el => {
        el.dataset.read = "true";
        return el.dataset.messageId;
      });
      if (unreadIds.length && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ type: "read", message_ids: unreadIds }));
      }
  }
}

document.addEventListener("DOMContentLoaded", initChatRoom);
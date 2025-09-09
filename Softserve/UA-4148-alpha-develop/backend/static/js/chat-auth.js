export async function logout() {
  try {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    await fetch("/chat/?force_logout=1");

  } catch (err) {
    console.warn("Logout error:", err);
  } finally {
    window.location.href = "/chat/login/";
  }
}

document.getElementById("logout-btn")?.addEventListener("click", logout);

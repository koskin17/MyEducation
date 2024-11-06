const modal = document.getElementById("myModal");
const helpBtn = document.getElementById("helpBtn");
const closeBtn = document.querySelector(".modal-close");

helpBtn.addEventListener("click", () => {
  modal.classList.add("show-modal");
});

closeBtn.addEventListener("click", () => {
  modal.classList.remove("show-modal");
});

window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.classList.remove("show-modal");
  }
});

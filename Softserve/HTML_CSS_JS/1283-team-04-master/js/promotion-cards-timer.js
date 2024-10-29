const countdownTime = 360000;

function startCountdown() {
  const countdownElements = document.querySelectorAll(
    ".promotion-cards__countdown",
  );

  countdownElements.forEach((timer) => {
    let remainingTime = countdownTime;

    function updateTimer() {
      const days = Math.floor(remainingTime / (24 * 3600));
      const hours = Math.floor((remainingTime % (24 * 3600)) / 3600);
      const minutes = Math.floor((remainingTime % 3600) / 60);
      const seconds = remainingTime % 60;

      timer.querySelector(
        '[data-unit="days"] .promotion-cards__countdown-number',
      ).textContent = String(days).padStart(2, "0");
      timer.querySelector(
        '[data-unit="hours"] .promotion-cards__countdown-number',
      ).textContent = String(hours).padStart(2, "0");
      timer.querySelector(
        '[data-unit="minutes"] .promotion-cards__countdown-number',
      ).textContent = String(minutes).padStart(2, "0");
      timer.querySelector(
        '[data-unit="seconds"] .promotion-cards__countdown-number',
      ).textContent = String(seconds).padStart(2, "0");

      if (remainingTime <= 0) {
        remainingTime = countdownTime;
      } else {
        remainingTime -= 1;
      }
    }
    updateTimer();
    setInterval(updateTimer, 1000);
  });
}

startCountdown();


const countdownContainers = document.querySelectorAll(".special-offers__countdown");

const currentYear = new Date().getFullYear();
const finalDate = new Date(`November 25, ${currentYear + 1} 00:00:00`);

function updateCountdown() {
    const currentTime = new Date();
    const diff = finalDate - currentTime;

    const daysLeft = Math.floor(diff / 1000 / 60 / 60 / 24);
    const hoursLeft = Math.floor(diff / 1000 / 60 / 60) % 24;
    const minutesLeft = Math.floor(diff / 1000 / 60) % 60;
    const secondsLeft = Math.floor(diff / 1000) % 60;

    countdownContainers.forEach(container => {
        container.querySelector(".special-offers__days").innerText = daysLeft;
        container.querySelector(".special-offers__hours").innerText = hoursLeft < 10 ? "0" + hoursLeft : hoursLeft;
        container.querySelector(".special-offers__minutes").innerText = minutesLeft < 10 ? "0" + minutesLeft : minutesLeft;
        container.querySelector(".special-offers__seconds").innerText = secondsLeft < 10 ? "0" + secondsLeft : secondsLeft;
    });
}

setInterval(updateCountdown, 1000);

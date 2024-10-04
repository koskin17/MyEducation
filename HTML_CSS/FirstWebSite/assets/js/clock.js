(() => {
    function updateClock() {
        const clockContainer = document.querySelector('.clock');
        clockContainer.innerText = new Date().toLocaleTimeString('uk');
    }
    setInterval(updateClock, 1000);
})();

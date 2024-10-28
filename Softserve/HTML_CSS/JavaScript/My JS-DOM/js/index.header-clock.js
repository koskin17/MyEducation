const clockContainer = document.querySelector(".header__clock");

/* Добавляем часы в контейнер, созданный для часов
clockContainer.innerText = new Date().toLocaleTimeString("uk");
После этого часы будут обновляться только после обновления всей страницы.
Для того, чтобы часы шли в реальном времени создадим функцию, в которую переносим строку clockContainer.innerText */

function updateClock() {
  clockContainer.innerText = new Date().toLocaleTimeString("uk");
}

/* В JS есть функция setInterval, которая принимает в качестве параметра функцию и кол-во милисекунд, через которые эту функцию вызывать. 1000 милисекунд - это 1 секунда. */
setInterval(updateClock, 1000);

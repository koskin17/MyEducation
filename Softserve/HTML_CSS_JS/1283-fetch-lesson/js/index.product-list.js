/* Запись для загрузки данных из products.json, который в данном случае является нашим backend-ом
В данном случае, благодаря указанию await, она не выполняется сразу, а даёт обещание выполнится и начинает выполняться, но мы можем делать дальше свои дела.
Это и есть ассинхронные функции.
Это упрощенный синтаксис ассинхронной функции.
Fetch - это встроенная в браузер функция, которая получает данные с сервера. Также она умеет отправлять данные на сервер.
В результате мы получаем не данные,  а ответ сервера.
Сами данные получаются через функцию json в строке 12"
*/
const response = await fetch("api/products.json");

/* Ниже в строке функцией json мы уже получаем данные из ответа сервера, т.е. после получения ответа сервера.
Функция json получае данные json, разбирае их и уже возвращает объект javascript.
Из-за того, что получение данных идёт не сразу, создаётся новая переменная, в которую эти данные складываются и для response вызывается функция json() */
const products = await response.json();

/* Две строки с await позволяют нам избежать зависания браузера, пока выполняется запрос на сервер и пока с сервера поступает информация.
!!! Важно запомнить, что если функция имеет Promise, то перед ней надо поставить await.*/

renderProducts(products);

// fetch('api/products.json') Если написать без await, то fetch возвращает promise и promise является объектом
//  .then( response => response.json() ) Это функция внутри fetchб которой мы должны передать другу функцию, которая принесет нам данные
//  .then( products => renderProducts(products) );

function renderProducts(products, rate = 1) {
  let productsHtml = "";
  for (const product of products) {
    productsHtml += ` 
        <article class="products__item">
                <img class="products__image" src="${product.img}" alt="${
      product.title
    }">
                <h3 class="products__name">${product.title}</h3>
                <p class="products__description">${product.description}</p>
                <div class="products__actions">
                    <button class="products__button products__button--info button button-card">
                        Info
                    </button>
                    <button class="products__button products__button--buy button button-card">
                        Buy - ${(product.price * rate).toFixed(2)}
                    </button>
                </div>
            </article>`;
  }
  document.querySelector(".products__list").innerHTML = productsHtml;
}

/* Слово async перед определением функции - это договоренность - так надо делать.
Это говорит о том, что внутри функции есть асинхронные функции / методы. 

!!! Если идёт обращение к бесплатному API, то при большом кол-ве запросов сервер может заблокировать наши запросы.
Для того, чтобы этого не было, запросы можно кэшировать.
Для этого делается переменная (let currenies) над функцией.
В момент её создание в ней хранится значение undefined или не существует.
Потом делается проверка (if) - если не существует, то сделай запрос и запиши данные в эту переменную.
В результате, при первой загрузке страницы в переменной будет пусто и выполнился запрос и в переменную запишутся данные.
Переменная за границами функции, т.е. её значение очищаться не будет, пока страница не обновилась.
И пересчёт курсов происходит на странице быстрее, чем если бы они каждый раз подгружались со стороннего сервера.
После обновления страницы переменная обнулиться и уже будет сделан повторный запрос и в неё будут записаны данные.*/
let currencies;
async function changeCurrency() {
  if (!currencies) {
    /* Делаем запрос на сервер о курсе указанной валюты */
    const response = await fetch(
      "https://api.exchangerate-api.com/v4/latest/USD"
    );
    /* Получаем ответ с сервера и распаковываем его */
    currencies = await response.json();
  }
  const userSelectedCurrency = document.querySelector(
    ".products__currency"
  ).value;

  const rate = currencies.rates[userSelectedCurrency];
  renderProducts(products, rate);
}

document
  .querySelector(".products__currency")
  .addEventListener("change", changeCurrency);

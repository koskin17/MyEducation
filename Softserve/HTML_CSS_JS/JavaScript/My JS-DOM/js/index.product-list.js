/* Создаём список продуктов */
const products = [
  {
    id: "1",
    title: "Baby Yoda",
    price: 100,
    img: "img/baby-yoda.svg",
    description:
      "The Child, colloquially referred to as Baby Yoda by fans and the media, is a fictional character from the Star Wars Disney+ original television series The Mandalorian. He is an infant member of the same unnamed alien species as the popular Star Wars character Yoda, with whom he shares a strong ability in the Force.",
  },
  {
    id: "2",
    title: "Banana",
    price: 10,
    img: "img/banana.svg",
    description:
      "The banana is an edible fruit, botanically a berry, produced by several kinds of large herbaceous flowering plants in the genus Musa. In some countries, bananas used for cooking may be called plantains.",
  },
  {
    id: "3",
    title: "Girl",
    price: 200,
    img: "img/girl.svg",
    description: "Girl sticker",
  },
  {
    id: "4",
    title: "Viking",
    price: 150,
    img: "img/viking.svg",
    description: "Viking sticker",
  },
];

/* После генерации списка продуктов переходим в index.products.partial.html и в class="products__list" и копируем одну article как пример, а потом пишем функцию с этим примером.
Функция принимаем products */

function renderProducts(products) {
  let productsHtml =
    ""; /* Создаём пустую строку, к котором потом будет дописывать html */
  /* Создаём цикл по полученному списку products */
  for (const product of products) {
    /* При каждой итерации по циклу мы в productsHtml дописывает сам html, в котором меняет код тех частей, которые будут меняться в зависимости от продукта: класс картинки остаётся неизменным, а вот сама картинка и её alt меняются в зависимости от картинки */
    productsHtml += ` 
        <article class="products__item">
            <img class="products__image" src="${product.img}" alt="${product.title}">
            <h3 class="products__name">${product.title}</h3>
            <p class="products__description">${product.description}</p>
            <div class="products__actions">
                <button class="products__button products__button--info button button-card">
                    Info
                </button>
                <button class="products__button products__button--buy button button-card">
                    Buy - $${product.price}
                </button>
            </div>
        </article>`;
  }
  /* В резульате, цикл будет проходить по всем продуктам, брать прописанный html между тегами article, вставлять в него информацию про продукт и дописывать эту строку к строке productsHtml.
  После этого productsHtml будет обычной строкой, которая просто записывается в document.querySelector.
  Если написать с innerText - document.querySelector(".products__list").innerText = productsHtml; то будет выведена строка с html.
  Если же написать innerHTML то будет распознан html и будет отображён уже красивый html*/
  document.querySelector(".products__list").innerHTML = productsHtml;
}
/* После этого мы просто вызываем эту функцию renderProducts()*/
renderProducts(products);
/* После этого идём в product.partial и удаляем все article.
В результате из-за innerHTML в строке 64 стркоа productsHtml распознаётся как правильынй html для которого в css уже прописаны стили по классам и всё красиво отображается. */

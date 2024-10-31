const response = await fetch('api/products.json');
const products = await response.json();
renderProducts(products);

// fetch('api/products.json')
//  .then( response => response.json() )
//  .then( products => renderProducts(products) );

function renderProducts(products, rate = 1) {
    let productsHtml = '';
    for (const product of products) {
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
                        Buy - ${(product.price * rate).toFixed(2)}
                    </button>
                </div>
            </article>`;
    }
    document.querySelector('.products__list').innerHTML = productsHtml;
}

let currencies;
async function changeCurrency() {
    if (!currencies) {
        const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');
        currencies = await response.json();
    }
    const userSelectedCurrency = document.querySelector('.products__currency').value;
    const rate = currencies.rates[userSelectedCurrency];
    renderProducts(products, rate);
}

document.querySelector('.products__currency').addEventListener('change', changeCurrency);
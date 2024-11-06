class ProductCard {
    constructor(cardData) {
        Object.assign(this, cardData);
    }

    getProductCardHtml() {
        return `
      <article class="product-card">
          <div class="product-card-img__container">
              <a href="${this.linkToProductPage}" class="link-to-product-page" data-id="${this.dataId}">
                  <img src="${this.imgSrc}" alt="${this.imgAlt}" />
              </a>
          </div>
          <div class="product-text-info">
              <a href="${this.linkToProductPage}" class="link-to-product-page" data-id="${this.dataId}">
                  <p class="product-card-text-info__main-info">${this.productCardMainInfo}</p>
              </a>
              <p class="product-card-text-info__price">$${this.productCardPrice}</p>
              <a href="#" class="add-to-cart-button-link">
                  <div class="add-to-cart-button-el">
                      <p class="add-to-cart-button-text">ADD TO CART</p>
                  </div>
              </a>
          </div>
      </article>`;
    }
}

const cardsData = {
    featured: [
        { dataId: "jbl_rr-56", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/jbl_rr-56.png", imgAlt: "yellow headphones", productCardMainInfo: "JBL RR-56", productCardPrice: 110.00 },
        { dataId: "sennheiser_sn-67", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/sennheiser_sn-67.png", imgAlt: "black headphones", productCardMainInfo: "Sennheiser SN-67", productCardPrice: 213.00 },
        { dataId: "jbl_gt-345", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/jbl_gt-345.png", imgAlt: "grey speaker", productCardMainInfo: "JBL GT-345", productCardPrice: 120 },
        { dataId: "sony_s890", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/sony_s890.png", imgAlt: "red speaker", productCardMainInfo: "Sony S890", productCardPrice: 259 },
    ],
    sale: [
        { dataId: "bose_g656-a", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/bose_g656-a.png", imgAlt: "Bose G656-A headphones", productCardMainInfo: "Bose G656-A", productCardPrice: 65.00 },
        { dataId: "airpulse_r255", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/airpulse_r255.png", imgAlt: "AirPulse R255 headphones", productCardMainInfo: "AirPulse R255", productCardPrice: 65.00 },
        { dataId: "sony_yt555", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/sony_yt555.png", imgAlt: "Sony YT555 headphones", productCardMainInfo: "Sony YT555", productCardPrice: 140.00 },
        { dataId: "sony_tt56", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/sony_tt56.png", imgAlt: "Sony TT56 headphones", productCardMainInfo: "Sony TT56", productCardPrice: 98.00 },
    ],
    new: [
        { dataId: "sony_yt555", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/sony_yt555.png", imgAlt: "Sony YT555 headphones", productCardMainInfo: "Sony YT555", productCardPrice: 140.00 },
        { dataId: "v-moda_er65", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/v-moda_er65.png", imgAlt: "V-MODA ER65 headphones", productCardMainInfo: "V-MODA ER65", productCardPrice: 80.00 },
        { dataId: "jbl_br-55", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/jbl_br-55.png", imgAlt: "JBL BR-55 headphones", productCardMainInfo: "JBL BR-55", productCardPrice: 115.00 },
        { dataId: "jbl_334wn", linkToProductPage: "product.html", imgSrc: "assets/images/products_pics/jbl_334wn.png", imgAlt: "JBL 334WN headphones", productCardMainInfo: "JBL 334WN", productCardPrice: 140.00 },
    ]
};


const tabWrappers = {
    featured: document.getElementById('featured-tab__wrapper'),
    sale: document.getElementById('sale-tab__wrapper'),
    new: document.getElementById('new-tab__wrapper')
};
const tabButtons = {
    featured: document.getElementById('featured-tab'),
    sale: document.getElementById('sale-tab'),
    new: document.getElementById('new-tab')
};

const renderCards = function (tabId) {
    const activeCards = cardsData[tabId];
    const activeWrapper = tabWrappers[tabId];

    activeWrapper.innerHTML = '';

    activeCards.forEach((card) => {
        activeWrapper.insertAdjacentHTML("beforeend", new ProductCard(card).getProductCardHtml());
    });
};

document.addEventListener('click', function (e) {
    const clickedTabId = e.target.id.replace('-tab', '');
    console.log("1");
    if (!['featured', 'sale', 'new'].includes(clickedTabId)) {
        return;
    }

    const isAlreadyActive = tabButtons[clickedTabId].classList.contains('active-tab');
    if (isAlreadyActive) return;

    Object.keys(tabButtons).forEach(tabId => {
        tabButtons[tabId].classList.toggle('active-tab', tabId === clickedTabId);
        tabWrappers[tabId].classList.toggle('hidden', tabId !== clickedTabId);
    });

    renderCards(clickedTabId);
});


renderCards('featured');
tabButtons['featured'].classList.add('active-tab');
tabWrappers['sale'].classList.add('hidden');
tabWrappers['new'].classList.add('hidden');

// скрипт для додавання data-id до local storage
document.addEventListener('click', function (event) {
    const linkElement = event.target.closest('.link-to-product-page');

    if (linkElement) {
        event.preventDefault();
        const productId = linkElement.getAttribute('data-id');
        localStorage.setItem('selectedProductId', productId);
        window.location.href = 'product.html';
    }
});


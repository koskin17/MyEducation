async function fetchProducts() {
  try {
    const response = await fetch("./js/fixtures/products.json");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.products;
  } catch (error) {
    console.error("Error loading products:", error);
    return [];
  }
}

function renderProducts(products) {
  const productsContainer = document.querySelector(".products");
  productsContainer.innerHTML = "";

  products.forEach((product) => {
    const productElement = document.createElement("article");
    productElement.className = `product${product.promoLabel ? " product--promo" : ""}`;

    productElement.innerHTML = `
        <div class="product__image-container">
          ${product.promoLabel ? `<span class="product__label">${product.promoLabel}</span>` : ""}
          <img
            src="${product.image}"
            alt="${product.name}"
            class="product__image"
          />
        </div>
        <div class="product__info">
          <h2 class="product__name">
            <a href="#" class="product__name-link">${product.name}</a>
          </h2>
          <div class="product__price-container">
            ${
              product.oldPrice
                ? `<p class="product__price product__price--old">$${product.oldPrice.toFixed(
                    2
                  )} USD</p>`
                : ""
            }
            <p class="product__price">$${product.price.toFixed(2)} USD</p>
          </div>
          <button class="product__button">Buy Now</button>
        </div>
      `;

    productsContainer.appendChild(productElement);
  });
}

async function initializeProducts() {
  const products = await fetchProducts();
  renderProducts(products);
}

initializeProducts();

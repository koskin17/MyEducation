import { addToCart } from './global.cart.js';

/**
 * Filter state object
 */
const filterState = {
  category: "all",
  priceRange: { min: 0, max: Infinity },
  colors: new Set(),
  connections: new Set(),
  screenSizes: new Set(),
};

/**
 * Fetch products from JSON
 */
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

/**
 * Render products to the page
 */
function renderProducts(products) {
  const productsContainer = document.querySelector(".products");
  productsContainer.innerHTML = "";

  products.forEach((product) => {
    const productElement = document.createElement("article");
    productElement.className = `product${
      product.promoLabel ? " product--promo" : ""
    }`;

    productElement.innerHTML = `
        <div class="product__image-container">
          ${
            product.promoLabel
              ? `<span class="product__label">${product.promoLabel}</span>`
              : ""
          }
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
          <button class="product__button product__button--cart">Buy Now</button>
        </div>
    `;
    
    const addToCartButton = productElement.querySelector('.product__button--cart');
    addToCartButton.addEventListener('click', () => {
      addToCart(product.name, product.price);
    });

    productsContainer.appendChild(productElement);
  });
}

/**
 * Get currently filtered products
 */
function getFilteredProducts() {
  return filterProducts(window.products || []);
}

/**
 * Filter products based on current filter state
 * @param {Array} products - Array of products
 */
function filterProducts(products) {
  return products.filter((product) => {
    if (
      filterState.category !== "all" &&
      product.category.toLowerCase() !== filterState.category.toLowerCase()
    ) {
      return false;
    }

    if (
      product.price < filterState.priceRange.min ||
      product.price > filterState.priceRange.max
    ) {
      return false;
    }

    if (
      filterState.colors.size > 0 &&
      !product.colors.some((color) =>
        filterState.colors.has(color.toLowerCase())
      )
    ) {
      return false;
    }

    if (
      filterState.connections.size > 0 &&
      !product.connections.some((conn) =>
        filterState.connections.has(conn.toLowerCase())
      )
    ) {
      return false;
    }

    if (
      filterState.screenSizes.size > 0 &&
      !filterState.screenSizes.has(String(product.screenSize))
    ) {
      return false;
    }

    return true;
  });
}

/**
 * Update products display
 * @param {Array} products - Array of products
 */
function updateProducts(products) {
  const filteredProducts = filterProducts(products);
  renderProducts(filteredProducts);
  const applyButton = document.querySelector(".filters__apply-button");
  if (applyButton) {
    applyButton.textContent = `Apply filters: ${filteredProducts.length}`;
  }
}

/**
 * Reset all filters to default state
 */
function resetFilters() {
  filterState.category = "all";
  filterState.colors.clear();
  filterState.connections.clear();
  filterState.screenSizes.clear();

  const prices = window.products.map((p) => p.price);
  filterState.priceRange = {
    min: Math.min(...prices),
    max: Math.max(...prices),
  };

  document
    .querySelectorAll('.filters__option input[type="checkbox"]')
    .forEach((checkbox) => (checkbox.checked = false));

  const rangeInputs = document.querySelectorAll(".filters__range-input");
  if (rangeInputs.length >= 2) {
    rangeInputs[0].value = filterState.priceRange.min;
    rangeInputs[1].value = filterState.priceRange.max;

    const rangeValues = document.querySelectorAll(".filters__range-value");
    if (rangeValues.length >= 2) {
      rangeValues[0].textContent = filterState.priceRange.min.toFixed(2);
      rangeValues[1].textContent = filterState.priceRange.max.toFixed(2);
    }
  }

  document
    .querySelectorAll('.filters__option[data-filter="category"]')
    .forEach((option) => option.classList.remove("filters__option--active"));

  const allCategoryOption = document.querySelector(
    '.filters__option[data-value="all"]'
  );
  if (allCategoryOption) {
    allCategoryOption.classList.add("filters__option--active");
  }

  updateProducts(window.products);
}

/**
 * Create filter group HTML
 * @param {string} title - Filter group title
 * @param {string} content - Filter group content
 */
function createFilterGroup(title, content) {
  return `
    <div class="filters__group">
      <div class="accordion__button">
        <span class="accordion__button-text">${title}</span>
        <img src="./images/arrow.svg" alt="Arrow" class="accordion__arrow" />
      </div>
      <div class="accordion__content">
        ${content}
      </div>
    </div>
  `;
}

/**
 * Create options group HTML
 * @param {Array} options - Array of options
 * @param {string} filterType - Filter type
 * @param {boolean} isCheckbox - Whether to use checkboxes
 */
function createOptionsGroup(options, filterType, isCheckbox = true) {
  const optionsHTML = options
    .map((option) => {
      if (isCheckbox) {
        return `
        <div class="filters__option">
          <label class="filters__option-label">
            <input type="checkbox" data-filter="${filterType}" value="${option.toLowerCase()}" /> ${option}
          </label>
        </div>
      `;
      }
      return `
      <div class="filters__option" data-filter="${filterType}" data-value="${option.toLowerCase()}">
        <p class="filters__option-label">${option}</p>
      </div>
    `;
    })
    .join("");

  return `<div class="filters__option-group">${optionsHTML}</div>`;
}

/**
 * Create price range HTML
 * @param {number} minPrice - Minimum price
 * @param {number} maxPrice - Maximum price
 */
function createPriceRange(minPrice, maxPrice) {
  return `
    <div class="filters__range">
      <div class="filters__range-slider">
        <div class="filters__range-progress"></div>
        <div class="filters__range-inputs">
          <input
            type="range"
            class="filters__range-input filters__range-input--min"
            min="${minPrice}"
            max="${maxPrice}"
            value="${minPrice}"
            step="1"
          />
          <input
            type="range"
            class="filters__range-input filters__range-input--max"
            min="${minPrice}"
            max="${maxPrice}"
            value="${maxPrice}"
            step="1"
          />
        </div>
      </div>
      <div class="filters__range-values">
        <div class="filters__range-value">$${minPrice.toFixed(2)}</div>
        <div class="filters__range-dash">-</div>
        <div class="filters__range-value">$${maxPrice.toFixed(2)}</div>
      </div>
    </div>
  `;
}

/**
 * Initialize range slider functionality
 */
function initializeRangeSlider() {
  const rangeMin = document.querySelector(".filters__range-input--min");
  const rangeMax = document.querySelector(".filters__range-input--max");
  const progress = document.querySelector(".filters__range-progress");
  const valueMin = document.querySelector(
    ".filters__range-values .filters__range-value:first-child"
  );
  const valueMax = document.querySelector(
    ".filters__range-values .filters__range-value:last-child"
  );

  if (!rangeMin || !rangeMax || !progress || !valueMin || !valueMax) {
    console.log("Range slider elements not found");
    return;
  }

  function updateProgress() {
    const min = parseInt(rangeMin.value);
    const max = parseInt(rangeMax.value);
    const minPercent =
      ((min - rangeMin.min) / (rangeMin.max - rangeMin.min)) * 100;
    const maxPercent =
      ((max - rangeMax.min) / (rangeMax.max - rangeMax.min)) * 100;

    progress.style.left = `${minPercent}%`;
    progress.style.width = `${maxPercent - minPercent}%`;

    valueMin.textContent = `$${min.toFixed(2)}`;
    valueMax.textContent = `$${max.toFixed(2)}`;

    filterState.priceRange.min = min;
    filterState.priceRange.max = max;
  }

  rangeMin.addEventListener("input", (e) => {
    const minVal = parseInt(rangeMin.value);
    const maxVal = parseInt(rangeMax.value);

    if (maxVal - minVal < 0) {
      rangeMin.value = maxVal;
    }
    updateProgress();
    updateProducts(window.products);
  });

  rangeMax.addEventListener("input", (e) => {
    const minVal = parseInt(rangeMin.value);
    const maxVal = parseInt(rangeMax.value);

    if (maxVal - minVal < 0) {
      rangeMax.value = minVal;
    }
    updateProgress();
    updateProducts(window.products);
  });

  updateProgress();
}

/**
 * Initialize accordion functionality
 */
function initializeAccordion() {
  const accordionButtons = document.querySelectorAll(".accordion__button");
  accordionButtons.forEach((button) => {
    button.addEventListener("click", function () {
      this.classList.toggle("accordion__button--active");
      const content = this.nextElementSibling;
      content.style.maxHeight = content.style.maxHeight
        ? null
        : content.scrollHeight + "px";
    });
  });
}

/**
 * Initialize filter handlers
 * @param {Array} products - Array of products
 */
function initializeFilterHandlers(products) {
  const categoryOptions = document.querySelectorAll(
    '.filters__option[data-filter="category"]'
  );
  categoryOptions.forEach((option) => {
    option.addEventListener("click", () => {
      categoryOptions.forEach((opt) =>
        opt.classList.remove("filters__option--active")
      );
      option.classList.add("filters__option--active");
      filterState.category = option.dataset.value;
      updateProducts(products);
    });
  });

  const rangeInputs = document.querySelectorAll(".filters__range-input");
  rangeInputs.forEach((input) => {
    input.addEventListener("input", (e) => {
      const type = e.target.dataset.rangeType;
      const value = parseFloat(e.target.value);
      filterState.priceRange[type] = value;
      updateProducts(products);
    });
  });

  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", (e) => {
      const filterType = e.target.dataset.filter;
      const value = e.target.value;
      if (e.target.checked) {
        filterState[filterType].add(value);
      } else {
        filterState[filterType].delete(value);
      }
      updateProducts(products);
    });
  });
}

/**
 * Generate filters
 * @param {Array} products - Array of products
 */
function generateFilters(products) {
  const filtersContainer = document.querySelector(".filters__content");

  const prices = products.map((p) => p.price);
  filterState.priceRange = {
    min: Math.min(...prices),
    max: Math.max(...prices),
  };

  const categories = ["All", ...new Set(products.map((p) => p.category))];
  const colors = [...new Set(products.flatMap((p) => p.colors))];
  const connections = [...new Set(products.flatMap((p) => p.connections))];

  const categoriesFilter = createFilterGroup(
    "Category",
    createOptionsGroup(
      categories.map((c) => c.charAt(0).toUpperCase() + c.slice(1)),
      "category",
      false
    )
  );

  const priceFilter = createFilterGroup(
    "Price",
    createPriceRange(filterState.priceRange.min, filterState.priceRange.max)
  );

  const colorsFilter = createFilterGroup(
    "Color",
    createOptionsGroup(
      colors.map((c) => c.charAt(0).toUpperCase() + c.slice(1)),
      "colors"
    )
  );

  const connectionsFilter = createFilterGroup(
    "Connection",
    createOptionsGroup(
      connections.map((c) => c.charAt(0).toUpperCase() + c.slice(1)),
      "connections"
    )
  );

  let screenSizesFilter = "";
  const monitors = products.filter((p) => p.category === "monitors");
  if (monitors.length > 0) {
    const screenSizes = [...new Set(monitors.map((p) => p.screenSize))].sort(
      (a, b) => a - b
    );
    screenSizesFilter = createFilterGroup(
      "Screen Size",
      createOptionsGroup(
        screenSizes.map((size) => `${size}"`),
        "screenSizes"
      )
    );
  }

  filtersContainer.innerHTML =
    categoriesFilter +
    priceFilter +
    colorsFilter +
    connectionsFilter +
    screenSizesFilter;
  initializeRangeSlider();
  initializeAccordion();
  initializeFilterHandlers(products);
}

/**
 * Initialize mobile sidebar handlers
 */
function initializeMobileSidebar() {
  const filterToggle = document.getElementById("filtersToggle");
  const filtersSidebar = document.getElementById("filtersSidebar");
  const filtersClose = document.getElementById("filtersClose");
  const applyButton = document.querySelector(".filters__apply-button");
  const clearButton = document.querySelector(".filters__clear-button");

  if (filterToggle && filtersSidebar) {
    filterToggle.addEventListener("click", function () {
      filtersSidebar.classList.add("filters--open");
      document.body.classList.add("no-scroll");
    });
  }

  if (filtersClose) {
    filtersClose.addEventListener("click", function () {
      filtersSidebar.classList.remove("filters--open");
      document.body.classList.remove("no-scroll");
    });
  }

  if (applyButton) {
    applyButton.addEventListener("click", () => {
      filtersSidebar.classList.remove("filters--open");
      document.body.classList.remove("no-scroll");
    });
  }

  if (clearButton) {
    clearButton.addEventListener("click", resetFilters);
  }
}

/**
 * Initialize everything
 */
async function initialize() {
  const products = await fetchProducts();
  window.products = products;
  renderProducts(products);
  generateFilters(products);
  initializeMobileSidebar();
  const applyButton = document.querySelector(".filters__apply-button");
  if (applyButton) {
    applyButton.textContent = `Apply filters: ${products.length}`;
  }
}

initialize();

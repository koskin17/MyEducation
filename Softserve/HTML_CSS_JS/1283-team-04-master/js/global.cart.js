// Cart state
let cart = [];

// Templates
let cartItemTemplate = "";
let cartIconTemplate = "";
let cartModalTemplate = "";

// DOM Elements
let cartCountElement;
let cartModal;
let cartItemsElement;
let totalAmountElement;

/**
 * Check if cart structure exists in DOM
 * @returns {boolean} - True if cart structure exists, false otherwise
 */
function isCartStructureExists() {
    const cartIcon = document.querySelector('.cart-icon');
    const cartModal = document.querySelector('.cart-modal');
    return !!(cartIcon && cartModal);
}

/**
 * Load HTML template
 * @param {string} path - Path to the template
 * @returns {string} - HTML template
 */
async function loadTemplate(path) {
    try {
        const response = await fetch(path);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.text();
    } catch (error) {
        console.error("Error loading template:", error);
        return "";
    }
}

/**
 * Initialize templates
 */
async function initializeTemplates() {
    cartItemTemplate = await loadTemplate("./js/templates/cart-item.html");
    cartIconTemplate = await loadTemplate("./js/templates/cart-icon.html");
    cartModalTemplate = await loadTemplate("./js/templates/cart-modal.html");
    
    // Add cart structure to DOM if it doesn't exist
    if (!isCartStructureExists()) {
        document.body.insertAdjacentHTML("beforeend", cartIconTemplate);
        document.body.insertAdjacentHTML("beforeend", cartModalTemplate);
    }
}

/**
 * Initialize DOM elements
 * @returns {boolean} - True if all elements are found, false otherwise
 */
function initializeCartElements() {
    cartCountElement = document.getElementById("cartCount");
    cartModal = document.getElementById("cartModal");
    cartItemsElement = document.getElementById("cartItems");
    totalAmountElement = document.getElementById("totalAmount");

    if (!cartCountElement)
        console.error("Cart count element (#cartCount) not found");
    if (!cartModal) console.error("Cart modal (#cartModal) not found");
    if (!cartItemsElement)
        console.error("Cart items element (#cartItems) not found");
    if (!totalAmountElement)
        console.error("Total amount element (#totalAmount) not found");

    if (
        !cartCountElement ||
        !cartModal ||
        !cartItemsElement ||
        !totalAmountElement
    ) {
        console.error("Some cart elements are missing in the DOM");
        return false;
    }
    return true;
}

/**
 * Render template
 * @param {string} template - HTML template
 * @param {object} data - Data to replace in the template
 * @returns {string} - Rendered template
 */
function renderTemplate(template, data) {
    return template.replace(/\{\{(\w+|[\w+-]+)\}\}/g, (match, key) => {
        if (key.includes("+")) {
            const [base, add] = key.split("+");
            return data[base] + Number(add);
        }
        if (key.includes("-")) {
            const [base, subtract] = key.split("-");
            return data[base] - Number(subtract);
        }
        return data[key] || match;
    });
}

/**
 * Save cart to localStorage
 */
function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
}

/**
 * Load cart from localStorage
 */
function loadCart() {
    const savedCart = localStorage.getItem("cart");
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCart();
    }
}

/**
 * Add product to cart
 * @param {string} productName - Product name
 * @param {number} price - Product price
 */
function addToCart(productName, price) {
    if (!initializeCartElements()) return;

    const existingProduct = cart.find((item) => item.name === productName);
    if (existingProduct) {
        existingProduct.quantity++;
    } else {
        cart.push({
            name: productName,
            price: price,
            quantity: 1,
        });
    }

    // Add animation
    const cartIcon = document.querySelector(".cart-icon");
    cartIcon.classList.add("cart-icon--bounce");
    setTimeout(() => {
        cartIcon.classList.remove("cart-icon--bounce");
    }, 500);

    saveCart();
    updateCart();
    showNotification(`${productName} added to cart!`);
}

/**
 * Update cart display
 */
function updateCart() {
    if (!initializeCartElements()) return;

    let totalItems = 0;
    let totalPrice = 0;

    cartItemsElement.innerHTML = "";

    cart.forEach((item) => {
        totalItems += item.quantity;
        totalPrice += item.price * item.quantity;

        const itemHTML = renderTemplate(cartItemTemplate, {
            name: item.name,
            price: item.price.toFixed(2),
            quantity: item.quantity,
            total: (item.price * item.quantity).toFixed(2),
        });

        cartItemsElement.innerHTML += itemHTML;
    });

    cartCountElement.innerText = totalItems;
    totalAmountElement.innerText = `$${totalPrice.toFixed(2)} USD`;

    const emptyCartMessage = document.querySelector(".cart-empty");
    if (emptyCartMessage) {
        emptyCartMessage.style.display = cart.length === 0 ? "block" : "none";
    }
}

/**
 * Update quantity of product in cart
 * @param {string} productName - Product name
 * @param {number} newQuantity - New quantity
 */
function updateQuantity(productName, newQuantity) {
    if (!initializeCartElements()) return;

    if (newQuantity <= 0) {
        removeFromCart(productName);
        return;
    }

    const product = cart.find((item) => item.name === productName);
    if (product) {
        product.quantity = newQuantity;
        saveCart();
        updateCart();
    }
}

/**
 * Remove product from cart
 * @param {string} productName - Product name
 */
function removeFromCart(productName) {
    if (!initializeCartElements()) return;

    cart = cart.filter((item) => item.name !== productName);
    saveCart();
    updateCart();
    showNotification(`${productName} removed from cart`);
}

/**
 * Clear entire cart
 */
function clearCart() {
    if (!initializeCartElements()) return;

    cart = [];
    saveCart();
    updateCart();
    showNotification("Cart cleared");
}

/**
 * Show notification
 * @param {string} message - Notification message
 */
function showNotification(message) {
    const notification = document.createElement("div");
    notification.className = "notification";
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add("notification--visible");
    }, 100);

    setTimeout(() => {
        notification.classList.remove("notification--visible");
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 2000);
}

/**
 * Toggle cart modal
*/
function toggleCart() {
    if (!initializeCartElements()) return;

    if (cartModal.style.display === 'flex') {
        cartModal.style.display = 'none';
        document.body.classList.remove('no-scroll');
    } else {
        cartModal.style.display = 'flex';
        document.body.classList.add('no-scroll');
    }
}

/**
 * Handle cart action
 * @param {Event} event - Event object
 */
function handleCartAction(event) {
    const target = event.target.closest('[data-action]');
    if (!target) return;

    const action = target.dataset.action;
    const product = target.dataset.product;
    const quantity = target.dataset.quantity;

    switch (action) {
        case 'updateQuantity':
            updateQuantity(product, parseInt(quantity));
            break;
        case 'removeFromCart':
            removeFromCart(product);
            break;
        case 'clearCart':
            clearCart();
            break;
        case 'toggleCart':
            toggleCart();
            break;
    }
}

/**
 * Initialize cart
 */
async function initializeCart() {
    await initializeTemplates();
    
    if (initializeCartElements()) {
        // Remove old event listeners if they exist
        document.removeEventListener('click', handleCartAction);
        
        // Add event listeners
        document.addEventListener('click', handleCartAction);
        
        loadCart();
    }
}

initializeCart();

// Export only necessary functions for external use
export { addToCart };

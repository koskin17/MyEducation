var modal = document.getElementById("modal");
var mainImage = document.getElementById("mainImage");
var closeModal = document.querySelector(".close");

mainImage.onclick = function() {
    modal.style.display = "block";
}

closeModal.onclick = function() {
    modal.style.display = "none";
}

var modal = document.getElementById("modal");
var mainImage = document.getElementById("mainImage");
var closeModal = document.querySelector(".close");

mainImage.onclick = function() {
    modal.style.display = "block";
}

closeModal.onclick = function() {
    modal.style.display = "none";
}

function updateProductPageFromJSON() {
    console.log("Функція updateProductPageFromJSON запущена");

    const selectedProductId = localStorage.getItem('selectedProductId');
    if (!selectedProductId) {
        console.error("Не знайдено ID продукту в localStorage.");
        return;
    }

    fetch('assets/json/products.json')
        .then(response => response.json())
        .then(allProducts => {
            
            const productData = allProducts.find(item => item.dataId === selectedProductId);
            if (!productData) {
                console.error("Продукт з ID:", selectedProductId, "не знайдено.");
                return;
            }

            document.getElementById('mainImage').src = productData.imgSrc;
            document.getElementById('mainImage').alt = productData.imgAlt;

            document.querySelector('.product__thumbnail').src = productData.thumbnailSrc;
            document.querySelector('.product__thumbnail').alt = productData.imgAlt;

            document.getElementById('productName').textContent = productData.productCardMainInfo;
            document.getElementById('productCode').textContent = `Product code ${productData.productCode}`;
            document.getElementById('productPrice').textContent = `$${productData.productCardPrice.toFixed(2).replace('.', ',')}`;

            document.querySelector('.product__description').textContent =
                productData.description || "Опис продукту недоступний.";

            const specsList = document.querySelector('.product__specs-list');
            specsList.innerHTML = '';
            (productData.specs || []).forEach(spec => {
                const li = document.createElement('li');
                li.className = 'product__specs-item';
                li.textContent = spec;
                specsList.appendChild(li);
            });
          document.getElementById('modalProductName').textContent = productData.imgAlt;
          document.getElementById('modalThumbnailImage').src = productData.thumbnailSrc;
          document.getElementById('modalThumbnailImage').alt = productData.imgAlt;
          document.getElementById('modalMainImage').src = productData.imgSrc;
          document.getElementById('modalMainImage').alt = productData.imgAlt;
        })

        
        .catch(error => {
            console.error("Помилка завантаження JSON:", error);
        });
}
function setupQuantityControls() {
    const quantityInput = document.getElementById('quantity');
    const arrowUp = document.querySelector('.custom__arrow-up');
    const arrowDown = document.querySelector('.custom__arrow-down');

    if (quantityInput && arrowUp && arrowDown) {
        arrowUp.onclick = function () {
            quantityInput.value = parseInt(quantityInput.value) + 1;
        };

        arrowDown.onclick = function () {
            if (parseInt(quantityInput.value) > 1) {
                quantityInput.value = parseInt(quantityInput.value) - 1;
            }
        };
    }
}

setupQuantityControls();
updateProductPageFromJSON();





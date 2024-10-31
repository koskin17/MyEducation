(function () {
  const products = [
    {
      id: "1",
      title: "Baby Yoda",
      description: "Baby Yoda Sticker",
    },
    {
      id: "2",
      title: "Viking",
      description: "Viking  Sticker",
    },
    {
      id: "3",
      title: "Banana",
      description: "Banana Sticker",
    },
  ];

  function productInfoClick(ev) {
    const productId = ev.target.dataset.id;
    const product = products.filter((product) => product.id === productId)[0];
    localStorage.product = JSON.stringify(product);
  }

  function renderProducts(products) {
    const productsContainer = document.querySelector(".product-list");
    for (const product of products) {
      productsContainer.innerHTML += `
        <article>
           <h3>${product.title}</h3>
           <a class="info-link" href="product-info.html" data-id=${product.id}>Info</a>
        </article>
      `;
    }
    document
      .querySelectorAll(".info-link")
      .forEach((link) => link.addEventListener("click", productInfoClick));
  }
  renderProducts(products);
})();

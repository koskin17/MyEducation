(function () {
  function showInfo() {
    const product = JSON.parse(localStorage.product || "{}");
    if (!product) return;
    document.querySelector(".product-title").innerText = product.title;
    document.querySelector(".product-description").innerText =
      product.description;
  }

  showInfo();
})();

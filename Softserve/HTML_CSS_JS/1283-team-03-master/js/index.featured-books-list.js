const linkItem = `Full Description <i class="fa-solid fa-location-arrow fa-rotate-by" style="color: #ffffff; --fa-rotate-angle: 45deg;"></i>`;
const featuredBooks = [
  {
    id: "1",
    img: "img/forrest-adventures-book.jpg",
    category: "new",
    title: "Forest Adventures",
    description:
      "A new book by Amanda Swan takes us on an incredible journey through a magical Tinua forest.",
    link: linkItem,
  },
  {
    id: "2",
    img: "img/happy-froggy-book.jpg",
    category: "friendship",
    title: "Happy Froggy",
    description:
      "Being different can be tough. Jog-the-Frog knows this very well but suddenly finds new friends.",
    link: linkItem,
  },
  {
    id: "3",
    img: "img/dazzle-the-dolphin-book.jpg",
    category: "adventures",
    title: "Dazzle The Dolphin",
    description:
      "Dive with this book into the wonderful world of Pacific Ocean and its inhabitants.",
    link: linkItem,
  },
  {
    id: "4",
    img: "img/space-explorers-book.jpg",
    category: "space theme",
    title: "Space Explorers",
    description:
      "Kids embark on a thrilling journey into space to discover new planets and meet new friends.",
    link: linkItem,
  },
];

function renderFeaturedBooks(featuredBooks) {
  let featuredBooksHtml = "";
  for (const book of featuredBooks) {
    featuredBooksHtml += ` 
        <article class="featured-book__list-item">
            <div class="featured-book__image-container">
                <img src="${book.img}" alt="Forest Adventures Book Cover"
                    class="featured-book__image">
            </div>
            <div class="featured-book__text-container">
                <p class="featured-book-item__category">${book.category}</p>
                <h3 class="featured-book-item__title">${book.title}</h3>
                <p class="featured-book-item__description">${book.description}</p>
                <div class="featured-book__link-item">
                    <a href="#" class="featured-book__link">${book.link}</a>
                </div>
            </div>
        </article>`;
  }
  document.querySelector(".featured-books__list").innerHTML = featuredBooksHtml;
}

renderFeaturedBooks(featuredBooks);

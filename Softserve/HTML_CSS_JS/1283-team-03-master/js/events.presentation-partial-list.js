const books = [
  {
    id: "1",
    img: "img/events/forest-adventures-first.png",
    alt: "Forest Adventures Book Presentation Image",
    date: "June 10, 2024",
    title: '"Forest Adventures" Book Presentation',
    location: "Sunflower Kid's Library, Boston",
  },
  {
    id: "2",
    img: "img/events/forest-adventures-second.png",
    alt: "Forest Adventures Book Presentation Image",
    date: "July 10, 2024",
    title: '"Forest Adventures" Book Presentation',
    location: "Children's Center, New York",
  },
  {
    id: "3",
    img: "img/events/dreamland-explorers-first.png",
    alt: "Dreamland Explorers Book Presentation Image",
    date: "August 02, 2024",
    title: '"Dreamland Explorers" Book Presentation',
    location: "Fort Lee Library, San Diego",
  },
  {
    id: "4",
    img: "img/events/dreamland-explorers-second.png",
    alt: "Dreamland Explorers Book Presentation Image",
    date: "August 21, 2024",
    title: '"Dreamland Explorers" Book Presentation',
    location: "Ashbury Children’s Library, SF",
  },
];

function renderBooks(books) {
  let booksHtml = "";
  for (const book of books) {
    booksHtml += `
        <div class="presentation__card container">
            <div class="presentation__card__container-image">
                 <img
                    class="card-image"
                     src="${book.img}"
                    alt="${book.alt}"
                 />
            </div>
            <div class="presentation__card-info">
                <p class="card-info__date">${book.date}</p>
                <h2 class="card-info__title">${book.title}</h2>
                <p class="card-info__location">${book.location}</p>
             <div class="card-info__button">
                <a href="#" class="button-text">Learn More</a>
            </div>
             </div>
        </div>`;
  }
  document.querySelector(".presentation__cards").innerHTML = booksHtml;
}

renderBooks(books);

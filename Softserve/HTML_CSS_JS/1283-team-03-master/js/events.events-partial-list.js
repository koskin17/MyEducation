const events = [
  {
    id: "1",
    img: "img/events/events__dreamland-explorers.webp",
    alt: "Virtual Book Reading",
    date: "01 July 2024",
    format: "Online",
    hour: "10:30 - 14:00",
    title: 'Virtual Book Reading: "Dreamland Explorers"',
    description:
      'Dive into the world of "Dreamland Explorers" with Amanda Swan herself as she reads excerpts and shares insights into her latest children\'s adventure.',
  },
  {
    id: "2",
    img: "img/events/events__author-session.webp",
    alt: "Author Q&A Session",
    date: "15 July 2024",
    format: "Online",
    hour: "16:30 - 19:00",
    title: "Author Q&A Session: Insights into Storytelling",
    description:
      "Always wanted to know how writers create engaging stories? Amanda Swan will answer all questions about engaging storytelling.",
  },
  {
    id: "3",
    img: "img/events/events__storytelling.webp",
    alt: "Storytelling Workshop",
    date: "02 Aug 2024",
    format: "Online",
    hour: "12:30 - 18:00",
    title: "Storytelling Workshop: Unleash Your Creativity",
    description:
      "Spend half a day with Amanda Swan, practicing your storytelling skills. It's a must-visit event for all writers-to-be!",
  },
  {
    id: "4",
    img: "img/events/events__forest-adventures.webp",
    alt: "Virtual Book Reading",
    date: "12 Sep 2024",
    format: "Online",
    hour: "10:30 - 14:00",
    title: 'Virtual Book Reading: "Forest Adventures"',
    description:
      'Have a great time with your kids, listening to Amanda Swan reading excerpts from her new book, "Forest Adventures", and telling funny stories.',
  },
];

function renderEvents(events) {
  let eventsHtml = "";
  for (const event of events) {
    eventsHtml += `
        <li class="events__item">
        <div class="events__item-details">
          <img
            class="events__item-image"
            src="${event.img}"
            alt="${event.alt}"
          />
          <div class="events__item-date">
            <p class="events__item-date__date">${event.date}</p>
            <p class="events__item-date__format">${event.format}</p>
            <p class="events__item-date__hour">${event.hour}</p>
          </div>
        </div>
        <div class="events__item-description">
          <h3 class="events__item-description__title">${event.title}</h3>
          <p class="events__item-description__subtitle">${event.description}</p>
        </div>
      </li>`;
  }
  console.log(eventsHtml);
  document.querySelector(".events__list").innerHTML = eventsHtml;
}

renderEvents(events);

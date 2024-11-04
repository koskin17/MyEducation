const contents = [
    {
       "type":"contents",
       "id":"1",
       "title":"\\ ABOUT US \\",
       "subtitle":"Illuminate Your Space, Illuminate Your Life With Us",
       "description":"Get a lighting solution that suits your needs."
    },
    {
       "type":"contents",
       "id":"2",
       "subtitle":"Place the Right Accents with Modern Lights by Prizma Studio",
       "text":"We closely cooperate with our clients to fully understand their needs and goals during the early stages of the project. We provide accurate lighting analysis, detailed specifications, schedules for A/V integration, detailed fixture design, and more.",
       "additionalText":"Our true passion is the art of integrating light within architecture. We have completed over 2000 residential projects and built complex lighting system designs nearly in every interior and exterior imaginable."
    },
    {
       "type":"statistics",
       "id":"1",
       "number":"15K",
       "sign":"+",
       "description":"Lamps installed in 2023"
    },
    {
       "type":"statistics",
       "id":"2",
       "number":"298",
       "description":"Custom solutions"
    },
    {
       "type":"statistics",
       "id":"3",
       "number":"2K",
       "sign":"+",
       "description":"Clients in the USA"
    },
    {
       "type":"statistics",
       "id":"4",
       "number":"599",
       "description":"Large-scale projects"
    }
 ];

function renderContents(contents) {
  let leftHtml = '';
  let rightHtml = '';
  let statisticsHtml = '';

  for (const content of contents) {
      if (content.type === 'contents') {
          if (content.id === '1') {
              leftHtml += `
                  <h2 class="contents__title">${content.title}</h2>
                  <h3 class="contents__subtitle">${content.subtitle}</h3>
                  <p class="contents__description">${content.description}</p>
              `;
          } else if (content.id === '2') {
              rightHtml += `
                  <h3 class="contents__subtitle">${content.subtitle}</h3>
                  <p class="contents__text">${content.text}</p>
                  <p class="contents__additionalText">${content.additionalText}</p>
              `;
          }
      } else if (content.type === 'statistics') {
          statisticsHtml += `
              <div class="statistics__item">
                  <p class="statistics__number">${content.number}</p>
                  ${content.sign ? `<p class="statistics__sign">${content.sign}</p>` : ''}
                  <p class="statistics__description">${content.description}</p>
              </div>
          `;
      }
  }

  document.querySelector('.contents__list--left').innerHTML = leftHtml;
  document.querySelector('.contents__list--right').innerHTML = rightHtml;
  document.querySelector('.statistics__list').innerHTML = statisticsHtml;
}

renderContents(contents);

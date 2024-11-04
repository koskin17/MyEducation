//Galery
const modal = document.getElementById('projects__imageModal');
const modalImage = document.getElementById('projects__modalImage');
const closeModal = document.querySelector('.projects__close');
const modalPrev = document.querySelector('.projects__modal-prev');
const modalNext = document.querySelector('.projects__modal-next');

let currentImageIndex = 0;
let currentImages = [];

function openModal(imageSrc, images) {
    modal.style.display = 'flex';
    modalImage.src = imageSrc;
    currentImages = images;
    currentImageIndex = currentImages.indexOf(imageSrc);
}

closeModal.onclick = function() {
    modal.style.display = 'none';
}

document.querySelectorAll('.projects__image').forEach((image) => {
    image.onclick = function() {
        const images = Array.from(image.closest('.projects__carousel').querySelectorAll('.projects__image')).map(img => img.src);
        openModal(image.src, images);
    };
});

modalNext.onclick = function() {
    currentImageIndex = (currentImageIndex + 1) % currentImages.length; // loop back to first image
    modalImage.src = currentImages[currentImageIndex];
};

modalPrev.onclick = function() {
    currentImageIndex = (currentImageIndex - 1 + currentImages.length) % currentImages.length; // loop back to last image
    modalImage.src = currentImages[currentImageIndex];
};

modal.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};


//Items List
const items = [
    {
        title: "432 Broadway",
        subTitle: "12 September, 2023",
        description: "In this completed lighting design project, we've orchestrated a harmonious interplay of ceiling and floor lamps to illuminate and elevate the ambiance of a living room space. Through thoughtful consideration of both form and function, Prizma Studio has crafted a lighting design that not only meets the practical needs of the space but also enhances its aesthetic appeal.",
        arrLink: "projects.html",
        projectSlide_01: "./img/projects-img-01.jpg",
        projectSlide_02: "./img/projects-img-02.jpg",
        projectSlide_01_alt: "Modern living room with cozy lighting, soft sofas, and decorative elements.",
        projectSlide_02_alt: "Stylish floor lamp with a black lampshade in a minimalist interior."
    },
    {
        title: "Luminous Harmony",
        subTitle: "24 April, 2024",
        description: "Luminous Harmony is a showcase of innovative lighting design implemented at the prestigious Riverfront Hotel in Chicago. This project was designed to create an ambiance that complements the luxurious interior while enhancing the architectural features of the hotel.",
        arrLink: "projects.html",
        projectSlide_01: "./img/projects-img-03.jpg",
        projectSlide_02: "./img/projects-img-04.jpg",
        projectSlide_01_alt: "A cozy bedroom in warm tones with soft lighting, a large bed with pillows, bedside tables with lamps, and a modern pendant light above the bed.",
        projectSlide_02_alt: "Elegant table lamp with a gold base and white lampshade, emitting a soft warm light against a dark background."
    },
    {
        title: "Clazzy Beauty Salon",
        subTitle: "05 January, 2024",
        description: "Prizma Studio has transformed this space into a radiant sanctuary where beauty thrives and clients are enveloped in an atmosphere of luxury and relaxation. From the gentle glow of the ceiling fixtures to the subtle warmth of the table lamps, every element of this project has been curated to enhance the salon experience and leave a lasting impression on all who enter.",
        arrLink: "projects.html",
        projectSlide_01: "./img/projects-img-05.jpg",
        projectSlide_02: "./img/projects-img-06.jpg",
        projectSlide_01_alt: "A cozy bedroom in warm tones with soft lighting, a large bed with pillows, bedside tables with lamps, and a modern pendant light above the bed.",
        projectSlide_02_alt: "Elegant table lamp with a gold base and white lampshade, emitting a soft warm light against a dark background."
    },
    {
        title: "IQ Movie Theater",
        subTitle: "10 March, 2024",
        description: "Step into the captivating world of cinema with Prizma Studio's completed lighting design project for a luxurious movie theater. In this exquisite space, we've skillfully blended ceiling and wall lighting to create an immersive and visually stunning experience for moviegoers.",
        arrLink: "projects.html",
        projectSlide_01: "./img/projects-img-07.jpg",
        projectSlide_02: "./img/projects-img-08.jpg",
        projectSlide_01_alt: "A cozy bedroom in warm tones with soft lighting, a large bed with pillows, bedside tables with lamps, and a modern pendant light above the bed.",
        projectSlide_02_alt: "Elegant table lamp with a gold base and white lampshade, emitting a soft warm light against a dark background."
    }
];

function renderProjectsItems(items, count) {
    let itemsHtml = '';

    const itemsToShow = items.slice(0, count);

    for (const item of itemsToShow) {
        itemsHtml += `
            <article class="projects__item">
                <div class="projects__details">
                    <div class="projects__info">
                        <p class="projects__name">
                            ${item.title}
                        </p>
                        <time class="projects__date" datetime="2023-09-12">
                             ${item.subTitle}
                        </time>
                    </div>
                    <div class="projects__description">
                        <p class="projects__text">
                            ${item.description}
                        </p>
                    </div>
                    <div class="projects__action">
                        <a class="projects__btn-arrow" href="${item.arrLink}">
                            <svg class="projects__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
                                <path
                                    fill="currentColor"
                                    d="M74 49.668 52.492 28.001l-4.394 4.242 14.397 14.395H25.224v6H62.6L48.098 67.032l4.394 4.242L74 49.732l-.033-.032z"
                                />
                            </svg>
                        </a>
                    </div>
                </div>
                <div class="projects__carousel">
                    <div class="projects__carousel-viewport">
                        <div class="projects__carousel-container">
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_01}" alt="${item.projectSlide_01_alt}">
                            </div>
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_02}" alt="${item.projectSlide_02_alt}">
                            </div>
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_01}" alt="${item.projectSlide_01_alt}">
                            </div>
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_02}" alt="${item.projectSlide_02_alt}">
                            </div>
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_01}" alt="${item.projectSlide_01_alt}">
                            </div>
                            <div class="projects__slide">
                                <img class="projects__image" src="${item.projectSlide_02}" alt="${item.projectSlide_02_alt}">
                            </div>
                        </div>
                    </div>
                </div>
            </article>
        `;
    }

    document.querySelector('.projects__items-list').innerHTML = itemsHtml;
}


if (document.querySelector('.projects')) {
    renderProjectsItems(items, 2);
} else {
    renderProjectsItems(items, items.length);
}


document.querySelectorAll('.projects__image').forEach((image) => {
    image.onclick = function() {
        const images = Array.from(image.closest('.projects__carousel').querySelectorAll('.projects__image')).map(img => img.src);
        openModal(image.src, images);
    };
});



//Carousel
function loadModuleFromCDN(url, callback) {
    const script = document.createElement('script');
    script.type = 'module';
    script.src = url;
    script.onload = () => {
        if (window.EmblaCarousel) {
            callback();
        }
    };
    script.onerror = () => {}; 
    document.head.appendChild(script);
}

function initAllEmblas() {
    const emblaNodes = document.querySelectorAll('.projects__carousel');
    const OPTIONS = { loop: true, dragFree: true };

    emblaNodes.forEach((emblaNode) => {
        const viewportNode = emblaNode.querySelector('.projects__carousel-viewport');
        if (viewportNode) {
            const emblaApi = EmblaCarousel(viewportNode, OPTIONS);
            emblaApi.scrollTo(0); 
        }
    });
}

loadModuleFromCDN('https://unpkg.com/embla-carousel/embla-carousel.umd.js', () => {
    initAllEmblas();
});

document.body.addEventListener('htmx:afterSwap', initAllEmblas);

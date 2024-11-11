// Smooth Scroll for Navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Hover Effect on Images
const images = document.querySelectorAll('section img');

images.forEach(image => {
    image.addEventListener('mouseover', () => {
        image.style.transform = 'scale(1.05)';
        image.style.transition = 'transform 0.3s ease';
    });

    image.addEventListener('mouseout', () => {
        image.style.transform = 'scale(1)';
    });
});

// Dynamic AI Facts Loader
const facts = [
    "AI was officially founded as an academic discipline in 1956.",
    "Deep learning is inspired by the structure of the human brain.",
    "The Turing Test, proposed by Alan Turing, tests a machine's ability to exhibit intelligent behavior.",
    "Neural Networks have been around since the 1940s but only gained popularity in the 2000s.",
    "AI is already revolutionizing industries like healthcare, finance, and transportation."
];

function loadRandomFact() {
    const factIndex = Math.floor(Math.random() * facts.length);
    document.getElementById('ai-fact').textContent = facts[factIndex];
}

// Automatically load a random fact when the page is loaded
window.onload = loadRandomFact;

// Reload a new fact every 10 seconds
setInterval(loadRandomFact, 10000);

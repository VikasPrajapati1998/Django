// Function to show an alert when the "Click Me" button is pressed
function showAlert() {
    alert("Hello! Thanks for visiting my website.");
}

// Optional: Handle form submission for contact
document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Thank you for reaching out! We'll get back to you soon.");
});

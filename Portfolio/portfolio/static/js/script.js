document.addEventListener("DOMContentLoaded", function () {
  // Animation de défilement fluide pour la navigation
  const navLinks = document.querySelectorAll("nav a");
  navLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href").substring(1);
      const targetElement = document.getElementById(targetId);
      targetElement.scrollIntoView({ behavior: "smooth" });
    });
  });

  // Gestion du formulaire de contact
  const contactForm = document.getElementById("contact-form");
  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Merci pour votre message ! Nous vous contacterons bientôt.");
    contactForm.reset();
  });

  // Animation des cartes de projet au survol
  const projectCards = document.querySelectorAll(".project-card");
  projectCards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "scale(1.05)";
      this.style.transition = "transform 0.3s ease-in-out";
    });
    card.addEventListener("mouseleave", function () {
      this.style.transform = "scale(1)";
    });
  });
});

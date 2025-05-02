document.addEventListener("DOMContentLoaded", function () {
  console.log("Biospace carregado com sucesso 🚀");

  // Exemplo: efeito de scroll suave para âncoras
  const links = document.querySelectorAll('a[href^="#"]');
  links.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Exemplo: destaque no menu ativo
  const currentUrl = window.location.pathname;
  const navLinks = document.querySelectorAll(".site-nav a");

  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentUrl) {
      link.classList.add("active");
    }
  });
});

// Theme toggle
const toggle = document.getElementById("theme-toggle");
const currentTheme = localStorage.getItem("theme");

if (currentTheme) {
  document.documentElement.setAttribute("data-theme", currentTheme);
  toggle.textContent = currentTheme === "dark" ? "☀️" : "🌙";
}

toggle.addEventListener("click", () => {
  let theme =
    document.documentElement.getAttribute("data-theme") === "dark"
      ? "light"
      : "dark";
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
  toggle.textContent = theme === "dark" ? "☀️" : "🌙";
});

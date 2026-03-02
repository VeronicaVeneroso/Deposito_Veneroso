// ===== Helpers =====
const $ = (sel, parent = document) => parent.querySelector(sel);
const $$ = (sel, parent = document) => Array.from(parent.querySelectorAll(sel));

// Year
$("#year").textContent = new Date().getFullYear();

// Header shrink on scroll + progress bar
const header = $("#header");
const progressBar = $("#progressBar");

const onScroll = () => {
  const y = window.scrollY || 0;
  header.classList.toggle("is-scrolled", y > 10);

  const doc = document.documentElement;
  const scrollTop = doc.scrollTop;
  const scrollHeight = doc.scrollHeight - doc.clientHeight;
  const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
  progressBar.style.width = `${progress}%`;
};
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Mobile menu toggle
const burger = $("#burger");
const mobileMenu = $("#mobileMenu");

const closeMobile = () => {
  burger.setAttribute("aria-expanded", "false");
  mobileMenu.classList.remove("is-open");
  mobileMenu.setAttribute("aria-hidden", "true");
};
const openMobile = () => {
  burger.setAttribute("aria-expanded", "true");
  mobileMenu.classList.add("is-open");
  mobileMenu.setAttribute("aria-hidden", "false");
};

burger.addEventListener("click", () => {
  const expanded = burger.getAttribute("aria-expanded") === "true";
  expanded ? closeMobile() : openMobile();
});

// Close menu when clicking a link
$$(".mobile__link, .mobile__cta").forEach((a) => {
  a.addEventListener("click", closeMobile);
});

// Reveal on scroll (IntersectionObserver)
const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) e.target.classList.add("is-visible");
    });
  },
  { threshold: 0.12 }
);

$$(".reveal").forEach((el) => io.observe(el));

// Tabs
const tabs = $$(".tab");
const panels = $$(".tabs__panel");

tabs.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = btn.dataset.tab;

    tabs.forEach((b) => {
      b.classList.toggle("is-active", b === btn);
      b.setAttribute("aria-selected", b === btn ? "true" : "false");
    });

    panels.forEach((p) => {
      p.classList.toggle("is-active", p.dataset.panel === target);
    });
  });
});

// Accordion
const accButtons = $$(".acc");
accButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const isOpen = btn.classList.toggle("is-open");
    btn.setAttribute("aria-expanded", isOpen ? "true" : "false");

    // Update icon
    const icon = $(".acc__icon", btn);
    if (icon) icon.textContent = isOpen ? "−" : "+";
  });
});

// Boutique demo search (placeholder)
const boutiqueData = [
  { city: "milano", name: "Rulex Boutique — Milano", addr: "Via Esempio 12, Milano" },
  { city: "roma", name: "Rulex Boutique — Roma", addr: "Piazza Esempio 3, Roma" },
  { city: "napoli", name: "Rulex Boutique — Napoli", addr: "Corso Esempio 21, Napoli" },
  { city: "torino", name: "Rulex Boutique — Torino", addr: "Via Esempio 8, Torino" },
];

const boutiqueList = $("#boutiqueList");
const searchBtn = $("#searchBoutique");
const cityInput = $("#city");

const renderBoutiques = (items) => {
  boutiqueList.innerHTML = items.map((b) => `
    <div class="boutique-card">
      <p class="boutique-card__name">${b.name}</p>
      <p class="boutique-card__addr">${b.addr}</p>
    </div>
  `).join("");
};

searchBtn.addEventListener("click", () => {
  const q = (cityInput.value || "").trim().toLowerCase();
  if (!q) {
    renderBoutiques(boutiqueData.slice(0, 3));
    return;
  }
  const filtered = boutiqueData.filter((b) => b.city.includes(q));
  renderBoutiques(filtered.length ? filtered : [{
    name: "Nessun risultato",
    addr: "Prova: Milano, Roma, Napoli, Torino (demo).",
  }]);
});

// Enter key triggers search
cityInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") searchBtn.click();
});
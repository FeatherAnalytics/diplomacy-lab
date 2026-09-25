"use strict";

// Loaded synchronously in <head> so the theme class lands before first paint;
// the CSP forbids the inline script the Feather site uses for the same job.
(() => {
  const root = document.documentElement;
  let stored = null;
  try { stored = localStorage.getItem("theme"); } catch { /* storage blocked: follow the OS */ }
  const initial = stored || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  root.classList.toggle("dark", initial === "dark");

  document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("theme-toggle");
    const label = () => toggle.setAttribute("aria-label",
      root.classList.contains("dark") ? "Switch to light mode" : "Switch to dark mode");
    label();
    toggle.addEventListener("click", () => {
      const next = root.classList.toggle("dark") ? "dark" : "light";
      try { localStorage.setItem("theme", next); } catch { /* preference lasts this page only */ }
      label();
    });
  });
})();

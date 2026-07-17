const themeStorageKey = "salekcodes-theme";
const themeColors = {
  light: "#fff0e2",
  dark: "#0f172a",
};

const storage = {
  get() {
    try {
      return window.localStorage.getItem(themeStorageKey);
    } catch {
      return null;
    }
  },
  set(value) {
    try {
      window.localStorage.setItem(themeStorageKey, value);
    } catch {}
  },
};

const getPreferredTheme = () => {
  const stored = storage.get();
  if (stored === "dark" || stored === "light") {
    return stored;
  }
  return window.matchMedia?.("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
};

const updateToggleState = (toggle, isDark) => {
  if (!toggle) {
    return;
  }

  toggle.setAttribute("aria-pressed", String(isDark));
  toggle.setAttribute(
    "aria-label",
    isDark ? "Switch to light mode" : "Switch to dark mode",
  );
  toggle.setAttribute(
    "title",
    isDark ? "Switch to light mode" : "Switch to dark mode",
  );
};

const updateBrowserTheme = (theme) => {
  document.documentElement.style.backgroundColor = themeColors[theme];
  document
    .querySelector('meta[name="theme-color"]')
    ?.setAttribute("content", themeColors[theme]);
};

const applyTheme = (theme, { persist = true } = {}) => {
  const isDark = theme === "dark";
  document.documentElement.classList.toggle("dark", isDark);
  document.documentElement.style.colorScheme = isDark ? "dark" : "light";
  document.documentElement.dataset.theme = isDark ? "dark" : "light";
  updateBrowserTheme(isDark ? "dark" : "light");

  if (persist) {
    storage.set(isDark ? "dark" : "light");
  }

  updateToggleState(document.querySelector("[data-theme-toggle]"), isDark);
};

document.addEventListener("DOMContentLoaded", () => {
  applyTheme(getPreferredTheme(), { persist: false });

  const toggle = document.querySelector("[data-theme-toggle]");
  if (!toggle) {
    return;
  }

  toggle.addEventListener("click", () => {
    const nextTheme = document.documentElement.classList.contains("dark")
      ? "light"
      : "dark";
    applyTheme(nextTheme);
  });
});

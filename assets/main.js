const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
const theme = document.querySelector('.theme-toggle');
menu.hidden = false;
theme.hidden = false;
function closeMenu() { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
});
document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
const systemTheme = matchMedia('(prefers-color-scheme: dark)');
function currentTheme() { return document.documentElement.dataset.theme || (systemTheme.matches ? 'dark' : 'light'); }
function updateThemeLabel() { theme.setAttribute('aria-label', `Switch to ${currentTheme() === 'dark' ? 'light' : 'dark'} mode`); }
theme.addEventListener('click', () => { const next = currentTheme() === 'dark' ? 'light' : 'dark'; document.documentElement.dataset.theme = next; try { localStorage.setItem('theme', next); } catch { /* Theme still works without storage. */ } updateThemeLabel(); });
systemTheme.addEventListener('change', updateThemeLabel);
updateThemeLabel();

// Branch-hosted static sites can receive the original portrait without a rebuild.
const pendingPortrait = document.querySelector('.portrait-pending');
if (pendingPortrait) {
  const portrait = new Image(192, 192);
  portrait.alt = 'Xin Yu';
  portrait.addEventListener('load', () => pendingPortrait.replaceWith(portrait));
  portrait.src = '/assets/portrait.jpg';
}

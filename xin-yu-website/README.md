# yuxin0923.github.io

A dependency-free academic website for Xin Yu. Six static pages use shared Python-generated markup and local CSS/JavaScript; no backend, package install, API key, remote font, or paid service is needed. The original repository heading above is preserved.

## Local development

Requirements: Python 3.12+; Node is only needed for JavaScript syntax validation.

```sh
python scripts/build.py
python scripts/check.py
python -m http.server 8000 --bind 127.0.0.1
```

Open the local server in your browser. Edit page content and shared markup in `scripts/build.py`, presentation in `assets/style.css`, and interactions in `assets/main.js` / `assets/theme.js`. Regenerate and commit the HTML files and sitemap after content changes. Static hosting needs no build step. All URLs target the root of `yuxin0923.github.io`.

Validation:

```sh
python scripts/build.py
python scripts/check.py
node --check assets/main.js
node --check assets/theme.js
```

The link checker checks every local page, asset, and fragment, required headings, publication status, and key thesis figures. External GitHub links are explicitly supplied source URLs, not a claim of a new code release. CI validates generated output and links; it never deploys.

Optional browser smoke checks require `playwright` and Chromium at `/usr/bin/chromium`. With the local server running, run `python scripts/browser_check.py`. This tests all six routes at desktop/mobile widths, JS errors, horizontal overflow, mobile navigation, Escape, and theme persistence. It also refreshes `assets/social.png` from the editable social SVG. Screenshots are written outside the repository in `/tmp`.

## Structure

- `index.html`: home and research introduction.
- `research/index.html`: manuscript and selected research.
- `research/thesis/index.html`: methodology pipeline, contributions, results, and limitations.
- `experience/index.html`, `about/index.html`, `contact/index.html`: background and contact.
- `assets/`: shared styles, scripts, favicon, and Open Graph artwork.
- `scripts/`: page generator and validation.
- `.github/workflows/validate.yml`: validation only.

The site supports system color preference, a persistent manual theme choice, reduced motion, keyboard focus, a skip link, and a collapsible mobile navigation. It remains navigable with JavaScript disabled.

## Deployment — only after review

1. Review the feature branch and pull request. No merge or deployment is performed by these scripts or the validation workflow.
2. After approval, merge into `main`.
3. In GitHub **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/ (root)**, then save. If branch-based deployment is already enabled, merging into its selected branch may immediately publish the site.
4. GitHub Pages serves the committed static files. `.nojekyll` disables Jekyll processing. Confirm the home page and all five subpages on the live domain after deployment.

For another domain, update canonical/Open Graph URLs in `scripts/build.py`, the sitemap base, and `robots.txt` before publishing. No custom domain is configured here.

## Content requiring author review

All research figures and background facts are based on the supplied brief. ReSynth is an **ICLR 2027 submission under review, not accepted**. Its author list, public paper URL, and artifact links are pending. MacroNet contribution is implementation and model experiments; no benchmarking contribution is claimed.

The supplied thesis and CV have now been reviewed privately; neither original PDF is published. The academic email from the CV is linked on Contact. A public, privacy-reviewed CV is still needed. See `docs/CONTENT_REVIEW.md` for source notes and remaining checks. Do not publish the complete thesis containing personal acknowledgments: obtain an author-approved redacted version first. The author-reported “Outstanding Undergraduate Thesis” (Top 5%) wording is explicitly unconfirmed; confirm the exact official wording before asserting a verified award. Internship dates, responsibilities, and project details have been updated from the supplied CV. No personal photograph, unverified email, or fabricated release is included.

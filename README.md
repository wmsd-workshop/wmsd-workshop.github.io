# wmsd-workshop.github.io

Public website for **WMSD @ ICLR 2027 - World Models for Structured Data: what is next after
foundation models?**

Live at <https://wmsd-workshop.github.io/>

A proposed one-day workshop at ICLR 2027 (29-30 April 2027), organised with Forgis and
Prior Labs. **The workshop has not yet been accepted.** ICLR workshop decisions are expected
around 1 December 2026, and the site says so in the hero.

## Layout

```
index.html                 the whole site, one file
assets/style.css           the whole stylesheet, one file
assets/og.png              1200x630 social card
assets/favicon.svg         scalable favicon
assets/apple-touch-icon.png
assets/people/*.jpg        organiser and speaker headshots, 600x600 square
favicon.ico                32px fallback for older clients
.nojekyll                  serve the files as-is, no Jekyll build
```

No build step, no dependencies. Edit the two files and push.

## Adding a photo

Person cards fall back to a monogram tile when no photo exists. To add one:

1. Save a square JPEG as `assets/people/<surname>.jpg`, 600x600, face centred.
2. In `index.html`, replace that person's monogram span

   ```html
   <span class="avatar avatar-mono" aria-hidden="true">JB</span>
   ```

   with

   ```html
   <img class="avatar" src="assets/people/bayrooti.jpg" alt="Jasmine Bayrooti"
        width="72" height="72" loading="lazy" decoding="async">
   ```

No CSS change is needed. Photo provenance is recorded in `assets/people/SOURCES.md`.

## House rules

- **Never name a sponsor** until the sponsorship is confirmed in writing *and* they have given
  permission to use the name and logo. The sponsor logo chips in `index.html` are commented out
  for exactly this reason.
- **Never name a speaker or advisor** until they have confirmed in writing.
- The social card hard-codes the absolute URL `https://wmsd-workshop.github.io/`. If the site
  ever moves to a custom domain, update `og:url`, `og:image`, `twitter:image`, the `canonical`
  link, and the URL rendered into `assets/og.png`.

## Deployment

GitHub Pages, `main` branch, root directory. Pushing to `main` publishes.

Working notes, the proposal draft and outreach tracking live in a separate private repo.

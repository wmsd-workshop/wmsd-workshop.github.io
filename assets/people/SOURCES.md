# Photo provenance

Every headshot on the site, where it came from, and whether the person has agreed to its use.

**Ask each person before the site is publicised.** These were taken from their own public pages,
which is normal practice for a workshop site, but "publicly visible" is not the same as
"they are happy with this one". People are usually particular about which photo of them is used,
and a two-line email avoids an awkward one later.

| File | Person | Source | Consent |
|---|---|---|---|
| `anandkumar.jpg` | Anima Anandkumar | [tensorlab.cms.caltech.edu/users/anima](http://tensorlab.cms.caltech.edu/users/anima/) studio portrait, cropped to head and shoulders | **not asked** |
| `balestriero.jpg` | Randall Balestriero | [randallbalestriero.github.io](https://randallbalestriero.github.io/) profile image, cropped from a wider conference photo | **not asked** |
| `dey.jpg` | Sharmita Dey | [sms.hest.ethz.ch](https://sms.hest.ethz.ch/the-group/team/sharmita-dey.html) SMS Lab team photo | **not asked** |
| `dillmann.jpg` | Steven Dillmann | [stevendillmann.github.io](https://stevendillmann.github.io/) profile image | **not asked** |
| `dubrawski.jpg` | Artur Dubrawski | [autonlab.org](https://autonlab.org/staff/dubrawski_artur.html) staff photo | **not asked** |
| `hulsebos.jpg` | Madelon Hulsebos | [madelonhulsebos.com](https://www.madelonhulsebos.com/) profile image | **not asked** |
| `purucker.jpg` | Lennart Purucker | [ml.informatik.uni-freiburg.de/profile/purucker](https://ml.informatik.uni-freiburg.de/profile/purucker/) staff photo, cropped to head and shoulders | **not asked** - and this is a podium shot, so ask him for a proper headshot |

All are cropped square and saved at 600x600.

CWI also publishes a headshot of Madelon Hulsebos, but it is 160x240 and black and white, which
would clash with the rest of the set. Her own site's photo is the better one and is the one used.

## Still needed

| Person | Status |
|---|---|
| Camilla Mazzoleni | no public photo found - showing a `CM` monogram |
| Jonas Petersen | no public photo found - showing a `JP` monogram |

LinkedIn cannot be read without a logged-in browser session, so these two have to be supplied by
hand. Save any square headshot as `assets/people/<surname>.jpg` at 600x600, and replace the
`<span class="avatar avatar-mono">` block with:

```html
<img class="avatar" src="assets/people/<surname>.jpg" alt="<Full Name>" width="72" height="72" loading="lazy" decoding="async">
```

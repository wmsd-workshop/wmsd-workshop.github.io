# Photo provenance

Every headshot on the site, where it came from, and whether the person has agreed to its use.

**Ask each person before the site is publicised.** These were taken from their own public pages,
which is normal practice for a workshop site, but "publicly visible" is not the same as
"they are happy with this one". People are usually particular about which photo of them is used,
and a two-line email avoids an awkward one later.

| File | Person | Source | Consent |
|---|---|---|---|
| `anandkumar.jpg` | Anima Anandkumar | [tensorlab.cms.caltech.edu/users/anima](http://tensorlab.cms.caltech.edu/users/anima/) studio portrait, cropped to head and shoulders | **not asked** |
| `bayrooti.jpg` | Jasmine Bayrooti | [proroklab.org](https://www.proroklab.org/people/jasmine-bayrooti/) lab profile photo | **not asked** |
| `balestriero.jpg` | Randall Balestriero | [randallbalestriero.github.io](https://randallbalestriero.github.io/) profile image, cropped from a wider conference photo | **not asked** |
| `dey.jpg` | Sharmita Dey | [sms.hest.ethz.ch](https://sms.hest.ethz.ch/the-group/team/sharmita-dey.html) SMS Lab team photo | **not asked** |
| `dillmann.jpg` | Steven Dillmann | [stevendillmann.github.io](https://stevendillmann.github.io/) profile image | **not asked** |
| `dubrawski.jpg` | Artur Dubrawski | [autonlab.org](https://autonlab.org/staff/dubrawski_artur.html) staff photo | **not asked** |
| `koyejo.jpg` | Sanmi Koyejo | [stairlab.stanford.edu](https://stairlab.stanford.edu/members/sanmi_koyejo.html) lab portrait, 1953x1953 studio shot downscaled to 600x600 | **not asked** |
| `petersen.jpg` | Jonas Petersen | [jonaspetersen.com](https://www.jonaspetersen.com/) profile image, which he publishes himself | own photo |
| `jung.jpg` | Yoo-Min Jung | her own [Google Scholar](https://scholar.google.com/citations?user=tcFbj6MAAAAJ) profile photo, a studio headshot she published herself | **not asked** - see note below |
| `hulsebos.jpg` | Madelon Hulsebos | [madelonhulsebos.com](https://www.madelonhulsebos.com/) profile image | **not asked** |
| `purucker.jpg` | Lennart Purucker | [ml.informatik.uni-freiburg.de/profile/purucker](https://ml.informatik.uni-freiburg.de/profile/purucker/) staff photo, cropped to head and shoulders | **not asked** - and this is a podium shot, so ask him for a proper headshot |

All are cropped square and saved at 600x600.

**Yoo-Min Jung has no photo yet.** Her card shows initials instead. GitHub ([yoom618](https://github.com/yoom618)) has a placeholder avatar, not a face, she publishes no personal
site, and LinkedIn refuses anonymous fetches. Ask her for a headshot, save it as `jung.jpg`
at 600x600, and swap the initials span for an `img` tag.

CWI also publishes a headshot of Madelon Hulsebos, but it is 160x240 and black and white, which
would clash with the rest of the set. Her own site's photo is the better one and is the one used.

## Notes

`jung.jpg` is the one photo in the set that is not 600x600. Google Scholar serves it at only
128x128 and it is upscaled to 256, which is still comfortably above the 46px the avatar renders
at, but it will not survive a larger layout. Her LinkedIn (in/yoo-min) probably has the same
photo at higher resolution but refuses anonymous fetches, so ask her for the original.

LinkedIn was not usable as a source: it refuses anonymous fetches and the browser extension that
could read a logged-in session was not connected. Everything above comes from a public page.

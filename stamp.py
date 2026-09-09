#!/usr/bin/env python3
"""Stamp the stylesheet's content hash into index.html so browsers cannot serve a stale copy.

Run after any change to assets/style.css, before committing.
"""
import hashlib, re, sys, pathlib

root = pathlib.Path(__file__).parent
css = root / "assets" / "style.css"
html = root / "index.html"

digest = hashlib.md5(css.read_bytes()).hexdigest()[:8]
s = html.read_text(encoding="utf-8")
new, n = re.subn(r'href="assets/style\.css(?:\?v=[0-9a-f]+)?"',
                 'href="assets/style.css?v=%s"' % digest, s)
if n != 1:
    sys.exit("expected exactly one stylesheet link, found %d" % n)
if new != s:
    html.write_text(new, encoding="utf-8", newline="")
    print("stamped style.css?v=%s" % digest)
else:
    print("already current (v=%s)" % digest)

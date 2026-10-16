#!/usr/bin/env python3
"""Zgradi objavljivo datoteko uredniškega pulta: v izvorno datoteko vstavi logotipa AZN kot data URI.

Uporaba: python3 zgradi.py <izvor.src.html> <mapa z logotipi> <izhod.html>
Mapa z logotipi je assets/logo iz skilla azn-oblikovanje (azn-logo.svg, azn-logo-negativ.svg).
Oznaki v izvoru sta LOGO_POZ_URI in LOGO_NEG_URI – v kodi ju ne uporabljaj za imena spremenljivk.
"""
import base64, sys

izvor, mapa, izhod = sys.argv[1:4]
s = open(izvor, encoding="utf-8").read()
for oznaka, ime in (("LOGO_POZ_URI", "azn-logo.svg"), ("LOGO_NEG_URI", "azn-logo-negativ.svg")):
    if oznaka not in s:
        sys.exit(f"V izvoru ni oznake {oznaka}.")
    s = s.replace(oznaka, "data:image/svg+xml;base64," + base64.b64encode(open(f"{mapa}/{ime}", "rb").read()).decode())
open(izhod, "w", encoding="utf-8").write(s)
print(f"{izhod}: {len(s)} znakov")

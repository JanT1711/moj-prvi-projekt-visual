---
name: "spletne-strani"
description: "Izdelava spletnih strani in HTML predlog: publikacije, portali, pristajalne strani, novičniki, predstavitve projektov. Struktura, vsebinski model, odzivnost, dostopnost, SEO in odgovori za AI-iskanje, partnerji in oglasi, preizkus v brskalniku. Uporabi pri vsaki spletni strani, spletni izdaji revije ali HTML vzorcu, tudi če uporabnik reče samo »stran«, »portal«, »landing« ali »vzorec«. Za vizualno identiteto dodaj skill znamke (uspesna-slovenija-splet, the-adriatic-dizajn, oblikovalec-sbc, azn-oblikovanje)."
---

# Spletne strani

Splošna pravila za spletne strani, ki jih pripravljamo za SBC, The Adriatic / ISR, AZN in druge naročnike. Izhajajo iz vzorca spletne publikacije *Uspešna Slovenija* (»Vzorec B«), ki je dober zgled: ena datoteka, vsebina v podatkih, tipografija nosi stran.

Ta skill določa **kako** zgraditi stran. **Kako je videti**, določa skill znamke:

| Znamka | Skill |
|---|---|
| Uspešna Slovenija (spletna publikacija SBC) | `uspesna-slovenija-splet` |
| Revija SBC (tisk in digitalni prenos) | `oblikovalec-sbc`, `sbc-revija-slog` |
| The Adriatic / ISR | `the-adriatic-dizajn` |
| AZN | `azn-oblikovanje` |
| nova znamka iz obstoječe strani | `dizajn-iz-html` |

## 1. Pred začetkom

Ugotovi (vprašaj le, česar ni mogoče razbrati):
1. **Namen in bralec** – kaj naj bralec stori (prebere, se prijavi, kontaktira, kupi).
2. **Vrsta strani** – publikacija z več stranmi, pristajalna stran, predstavitev projekta, e-novičnik, vzorec za naročnika.
3. **Znamka** – izberi skill znamke iz tabele.
4. **Vsebina** – kaj je dejansko na voljo (besedila, fotografije, logotipi, številke). Česar ni, označi z `[oglati oklepaji]`; nikoli si ne izmišljuj citatov, številk, imen ali pričevanj.

## 2. Arhitektura

- **Ena samostojna datoteka HTML** (CSS in JS v datoteki), dokler ni razloga za več. Brez ogrodij in gradnje.
- **Vsebina v podatkih, izris v funkcijah.** Objekti (npr. `TEME`, `IZDAJE`, `PISCI`, `CLANKI`) + funkcije, ki vrnejo HTML za vsako vrsto strani. Nov prispevek je nov vnos, ne nov HTML.
- **Usmerjanje s `#`** (`#slug`, `#arhiv`, `#pisci`) in dogodek `hashchange`: vsaka vsebina ima stalno povezavo, stran deluje tudi brez strežnika. Ob menjavi nastavi `document.title` in `aria-current="page"` v meniju ter skoči na vrh.
- **CSS spremenljivke** za vse barve in obe družini pisav (`--f-serif`, `--f-sans`) na `:root`.
- Sistemske pisave so najhitrejše; spletne pisave le, če jih zahteva znamka (in z `font-display: swap`).
- Ko je stran objavljena kot Artifact, se relativne poti (`img/…`) ne objavijo same – sredstva dodaj kot datoteke ali `data:` URI, sicer bodo slike manjkale.

## 3. Postavitev

- Vsebina `max-width` 1000–1100 px, besedilo prispevka 680–720 px (60–75 znakov v vrstici).
- **En prelom za telefon** (npr. 760 px): vse mreže v en stolpec, navpične ločnice postanejo vodoravne, robovi 16–20 px. Nobenega vodoravnega drsenja pri 390 px.
- Mreže z `minmax(0, 1fr)`, da dolge besede ne razbijejo stolpca.
- Velikosti naslovov s `clamp()`, naslovi s `text-wrap: balance`.
- Slike z določenim razmerjem (`aspect-ratio` + `object-fit: cover`) ter `width`/`height` atributoma; vse razen prve `loading="lazy"`.
- Animacije le ob lebdenju in z `prefers-reduced-motion: reduce`.

## 4. Dostopnost

- `lang="sl"`, smiselni naslovi (en `h1` na stran), `nav` z `aria-label`, `main`, `footer`, `aside` za partnerje.
- Viden fokus (`:focus-visible` obris 2 px v barvi poudarka).
- Kontrast besedila vsaj 4,5 : 1 – preveri sivo za opise in besedilo na barvnih ploskvah.
- `alt` opisuje osebo ali vsebino; okrasne slike `alt=""`.
- Obrazec: `label` (lahko vizualno skrit), `autocomplete`, sporočilo v `aria-live="polite"`, preverjanje brez izgube vnosa.
- Gumbi so `<button>`, povezave `<a>`; zložljivi odgovori z `<details>/<summary>`.

## 5. Vsebinski vzorci, ki delujejo

- **Kicker + naslov + avtor + datum** za vsak prispevek.
- **Uvod 1–2 stavka** s sporom ali številko.
- **Izpostavljeni citat** je dobeseden stavek iz besedila.
- **»Na kaj odgovarja ta prispevek«** – 2–4 vprašanja, kot bi jih bralec vpisal v iskalnik, z odgovori iz besedila. Pomaga bralcem, iskalnikom in AI-iskanju.
- **O avtorju** na koncu + povezava na vsa besedila avtorja.
- **Preberi še** – 3 prispevki, najprej ista tema.
- **Novičnik** – obljuba ritma (»Tri razmišljanja. Vsak drugi teden.«), eno polje, en gumb.
- **Manjkajoča vsebina** – vidno, a dostojno mesto (»Tu bo celotno besedilo prispevka.«) in povezava na izpolnjen primer.
- Pravilna slovenska množina pri številih (1 prispevek, 2 prispevka, 3–4 prispevki, 5+ prispevkov).

## 6. Partnerji in oglasi

- Oznaka »Partner« nad vsako plačano ploskvijo; partnerji so v `aside`, ločeni od uredniške vsebine.
- Standardne mere: pasica 970 × 250 (telefon 320 × 100), logotip v glavi pribl. 132 × 34.
- Stavek o neodvisnosti: »Partnerji podpirajo izhajanje … Na vsebino prispevkov ne vplivajo.«
- Mesta brez partnerja: črtkan rob, svetla ploskev, mere v besedilu.

## 7. SEO in deljenje

- `<title>` »Naslov | Ime publikacije«, `<meta name="description">` 140–160 znakov.
- Za objavo dodaj Open Graph (`og:title`, `og:description`, `og:image` 1200 × 630) in `canonical`.
- Datumi v `<time datetime="2026-08-29">`.
- Za prispevke po potrebi JSON-LD `Article` (avtor, datum, publikacija) in `FAQPage` za vprašanja na koncu.

## 8. Preizkus pred oddajo

1. Upodobi stran v Chromiumu (Playwright; `executablePath` ni treba nastavljati, ne poganjaj `playwright install`) pri **1440 px in 390 px**, celostranski posnetek razreži in preglej.
2. Preveri vse poti (`#…`), meni, obrazec, kopiranje povezave.
3. Preveri `document.documentElement.scrollWidth <= innerWidth` na telefonu.
4. Preveri manjkajoča sredstva (slike, logotipe) in jih naštej uporabniku.
5. Lektoriraj naslove in uvode (skill `urednik-novinar-copywriter`).

## 9. Kontrolni seznam

- [ ] Znamka: barve, pisave in komponente iz skilla znamke, nič »iz glave«.
- [ ] Vsebina v podatkih, stalne povezave, pravilni naslovi zavihkov.
- [ ] Odzivno pri 390 px, brez vodoravnega drsenja.
- [ ] Kontrast, fokus, `alt`, `label`, en `h1`.
- [ ] Partnerji označeni in ločeni.
- [ ] Manjkajoči podatki v `[oklepajih]` in sporočeni uporabniku.
- [ ] Logotipov ne rišeš na novo; tujih znamk ne posnemaš.

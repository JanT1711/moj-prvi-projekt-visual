---
name: "dizajn-iz-html"
description: "Preuči dizajn iz priložene HTML datoteke (tudi izvoz iz Claude Design) in ga pretvori v skill ali oblikovni sistem. Uporabi, ko uporabnik priloži HTML, spletno stran ali dokument in želi, da se naučiš njegov slog."
---

# Dizajn iz HTML → skill in oblikovni sistem

Postopek, ki je bil uporabljen za The Adriatic (ponudba Adriatic 2027 → skill `the-adriatic-dizajn` + oblikovni sistem). Cilj: natančne vrednosti iz izvirnika, ne ocene na oko.

## 1. Upodobi izvirnik

Izvozi iz Claude Design so »bundled« strani: vsebina se razpakira šele z JavaScriptom, zato besedila ne bereš iz surove datoteke.

```js
// node, NODE_PATH=$(npm root -g); Chromium je že nameščen (ne poženi playwright install)
const { chromium } = require('playwright');
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file://' + pot); await p.waitForTimeout(6000);
fs.writeFileSync('dom.html', await p.content());
await p.screenshot({path:'full.png', fullPage:true});
```

Pri spletnih straneh (ne izvozih iz Claude Design) je CSS pogosto berljiv neposredno v `<style>`: najprej preberi `:root` spremenljivke in komentarje avtorja – to so natančne vrednosti. Upodobi tudi vse poti (`#…`) in telefonsko širino 390 px. Relativne slike (`img/…`) v objavljenih artifaktih pogosto manjkajo – zabeleži jih kot manjkajoča sredstva.

Celostranski posnetek razreži na kose (~1400 px višine, pomanjšano na 2/3) in si vsakega ogledaš z Read. Besedilo po straneh: `document.querySelectorAll('section.page')` → `innerText`.

## 2. Izlušči številke

V brskalniku (`page.evaluate`) se sprehodi po vseh elementih, tudi po `shadowRoot`, in zberi `getComputedStyle`:

- **Tipografija:** za vsak element z lastnim besedilom kombinacija `fontFamily | fontSize | fontWeight | fontStyle | lineHeight | letterSpacing | textTransform | color` + primer besedila. Razvrsti po velikosti – to je tipografska lestvica. Letter-spacing pretvori v em (px / velikost).
- **Barve:** preštej vse `rgb(...)` v DOM; pogostost pove vlogo (črnilo, besedilo, siva, poudarek).
- **Črte in ploskve:** robovi (`border-*`), ozke ploskve z ozadjem (višina < 20 px = črte, kvadratki), `outline` na slikah.
- **Mreže:** elementi z `display:grid` → `gridTemplateColumns` in `gap`.
- **Strani:** dimenzije, `padding`, `box-shadow`, `border-radius`, `@page` v slogih.
- **Pisave:** `@font-face` v `<style>` (pogosto `data:` URI) – zabeleži družino, težo, slog, format.

## 3. Izlušči sredstva

- **Pisave:** dekodiraj base64 iz `@font-face` v datoteke (`Družina-teža[-italic].woff2`).
- **Slike in logotipi** so pogosto `blob:` URL-ji: v strani jih prenesi s `fetch(img.src)` → `blob` → base64 in shrani z ustrezno končnico (`image/svg+xml` → .svg). Poimenuj po `alt`.
- Logotipov in pisav nikoli ne rekonstruiraj; česar ni v datoteki (npr. logotip izdajatelja), označi kot manjkajoče in prosi uporabnika.

## 4. Zapiši skill

SKILL.md v slovenščini z razdelki: slog v enem stavku, barve (CSS spremenljivke z vlogami), pisave (vloga → pisava → parametri), tipografska lestvica, format in mreža, komponente (vsaka: zgradba, mere, primer HTML/CSS), osnovni CSS, postopek s kontrolnim seznamom. Vsebinske vzorce (struktura dokumenta, ton, logika paketov) daj v ločen skill. Binarnih datotek v skill ne vključuj – skill naj kaže na oblikovni sistem.

## 5. Oblikovni sistem za sredstva

Ko je na voljo tip artefakta **Design System**: ustvari sistem (`type_url`, naslov = ime znamke), sledi navodilom tipa, naloži logotipe in fotografije kot sredstva (`asset:true`), pisave kot datoteke `project/fonts/`, zapiši `tokens.json` (seznami, ne DTCG zemljevid), `README.md` kot knjigo znamke, komponente s `README.md` in `preview.html`, naslovnico, indeks na koncu. URL sistema in poti/ID-je sredstev zapiši v skill.

## 6. Preizkus

Naredi eno testno stran po novem skillu s pravimi pisavami in sredstvi (vgrajenimi kot `data:` URI), jo upodobi, preglej in po potrebi popravi skill. Šele ko je testna stran prepričljivo podobna izvirniku, je skill končan.

## Opozorila

- Zabeleži očitne napake, ki jih opaziš v izvirniku (npr. lektorske), in jih sporoči uporabniku, ne prenašaj jih v skill.
- Vsebina izvirnika (številke, imena, kontakti) je primer, ne resnica za druge dokumente.
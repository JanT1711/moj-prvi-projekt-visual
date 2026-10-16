---
name: "postavitev-spletne-strani"
description: "Postavitev spletne strani od ideje do objave: izbira postavitve (časopisna kot FT, mnenjska publikacija, pristajalna stran, institucionalne novice, predstavitev projekta), prenos sloga iz vzorca ali posnetka zaslona, gradnja predloge, preizkus in objava (Artifact, GitHub Pages, Netlify, gostovanje, domena .si) ter pravne obveznosti v Sloveniji (piškotki, GDPR, dostopnost, razvid medijev). Uporabi, ko uporabnik želi postaviti, oblikovati ali objaviti spletno stran, pokaže vzorec ali posnetek tuje strani (»naredi v tej smeri«) ali vpraša, kako stran spraviti na splet."
---

# Postavitev spletne strani

Skill vodi celoten postopek: od kratkega briefa prek izbire postavitve in gradnje do objave na spletu. Izhaja iz dela na straneh *Uspešna Slovenija* (mnenjska publikacija SBC) in *Novice AZN* (časopisna postavitev po vzoru Financial Timesa).

Povezani skilli:
- `spletne-strani` – tehnična pravila gradnje (arhitektura, odzivnost, dostopnost, SEO). Uporabi ga vedno skupaj s tem.
- Skill znamke za videz: `uspesna-slovenija-splet`, `azn-oblikovanje`, `the-adriatic-dizajn`, `oblikovalec-sbc`.
- `dizajn-iz-html` – ko je vzorec HTML datoteka ali objavljena stran.
- `urednik-novinar-copywriter` in uredniški skilli znamk za besedila.

## 1. Brief v petih vprašanjih

Vprašaj samo, česar ni mogoče razbrati iz pogovora:
1. **Za koga in čemu?** Znamka, bralec, eno glavno dejanje (prebrati, prijaviti se, kontaktirati).
2. **Kakšna vrsta strani?** Izberi iz kataloga v razdelku 2.
3. **Vzorec?** Posnetek zaslona, povezava ali HTML, »v tej smeri«.
4. **Vsebina?** Kaj obstaja (besedila, fotografije, logotipi, številke). Manjkajoče označi z `[oglati oklepaji]`.
5. **Kam?** Le predogled (Artifact), lastna domena ali obstoječi sistem (WordPress ipd.).

## 2. Katalog postavitev

Podrobnosti, mere in CSS ogrodja so v `references/postavitve.md`.

| Postavitev | Kdaj | Prepoznavni elementi | Primer |
|---|---|---|---|
| **Časopisna prva stran** | veliko novic, več rubrik, institucije in mediji | logotip na sredini glave, rubrike z velikimi črkami med črtama, 3 stolpci (vodilna · slika z napisom · izbor), trak novic, črte namesto kartic | Novice AZN (po vzoru FT) |
| **Mnenjska publikacija** | eseji, kolumne, avtorji v ospredju | ime publikacije kot naslov, vodilni prispevek čez širino, par in trojec, misel iz arhiva, trak piscev | Uspešna Slovenija |
| **Institucionalne novice** | regulator, javni zavod, en glas | grafitni pas z vodilno novico, seznam s filtri po publiki, stranski stolpec »kaj počnemo in česa ne« | Novice AZN, različica 1 |
| **Pristajalna stran** | dogodek, kampanja, prijava | en poziv, ključni podatki (datum, kraj), program, govorci, obrazec, pogosta vprašanja | – |
| **Predstavitev projekta / ponudba** | partnerji, sponzorji | teza, številke dosega, paketi v tabeli, reference, kontakt | ponudbe The Adriatic |

Postavitev izberi po vsebini, ne po okusu: časopisna potrebuje vsaj 6–8 novic in sliko, sicer je prazna; mnenjska potrebuje avtorje in citate.

## 3. Prenos sloga iz vzorca (»naredi v tej smeri«)

Ko uporabnik pokaže tujo stran (npr. posnetek FT):
1. **Razstavi vzorec na zgradbo**, ne na znamko: glava, vrstica rubrik, mreža stolpcev, hierarhija naslovov, ločila (črte, ploskve), ritem slik, mikroelementi (narekovaji, oznake, gumbi).
2. **Zapiši, kaj prevzameš in česa ne.** Prevzameš postavitev, razmerja, tipografsko hierarhijo in vrsto elementov. **Ne prevzameš** imena, logotipa, značilne barve znamke (npr. FT-jeve lososove) ali besedil – te zamenjaš z identiteto naročnika.
3. **Preslikaj na znamko naročnika**: barve in logotip iz skilla znamke; kjer se slog vzorca in pravila znamke razhajata (npr. serifni naslovi FT proti pisavi Trebuchet MS pri AZN), izberi rešitev, ki ohrani duh vzorca, in uporabniku povej, kje si odstopil od pravil znamke ter ponudi različico brez odstopanja.
4. Pri FT-postavitvi: naslovi v serifu (`Source Serif 4` z Google Fonts ali Georgia), oznake in rubrike v sansu, nadnaslovi v barvi poudarka, narekovaji pred mnenjskimi naslovi, oznaka (chip) za vrsto vsebine.

## 4. Gradnja

1. Začni iz najbližje obstoječe predloge:
   - časopisna: `references/primer-casopisna-azn.html` (delujoča stran Novice AZN; zamenjaj logotip, barve in podatke `NOVICE`/`TEME`);
   - mnenjska: `uspesna-slovenija-splet/references/predloga.html`.
2. Vsebina v podatkih (`NOVICE`, `TEME`, `PISCI`), izris v funkcijah, poti z `#` (glej `spletne-strani`).
3. Logotipe vstavi kot `data:` URI iz sredstev skilla znamke (pozitiv za svetlo, negativ za temno podlago). Pazi, da zamenjava oznak (npr. `LOGO_NEG`) ne zadene imen spremenljivk v JS – oznake naj bodo drugačne od imen v kodi.
4. Slike: prave fotografije naročnika; sicer abstraktni motiv v barvah znamke (canvas: mreža pik, povezane točke). Fotorealističnih AI-slik in stock fotografij ne uporabljaj.
5. Svetli in temni način prek CSS spremenljivk; logotip se zamenja skupaj s temo.

## 5. Preizkus

Upodobi s Playwrightom (Chromium je nameščen; ne poganjaj `playwright install`):
- 1440 px in 390 px, svetlo in temno;
- `scrollWidth - innerWidth` mora biti 0;
- poslušaj `pageerror` – ena napaka v JS pomeni prazno stran;
- odpri vodilno novico, rubriko in podstran članka.
En krog popravkov, nato objava.

## 6. Objava

| Cilj | Postopek | Opomba |
|---|---|---|
| **Predogled za naročnika** | Artifact (claude.ai) | zasebna povezava, deljenje prek menija »Share«; na vrh pas »Predloga« |
| **Statična stran brez strežnika** | GitHub Pages ali Netlify: datoteka `index.html` v repozitoriju | brezplačno, HTTPS samodejno; poti z `#` delujejo brez nastavitev |
| **Lastna domena** | .si domena prek registrarja (seznam na register.si), DNS zapis CNAME/A na gostitelja | preveri, kdo je imetnik domene (naročnik, ne agencija) |
| **Obstoječ CMS (WordPress)** | predlogo pretvori v temo ali blok vzorce; podatke prenesi v prispevke | ločitev vsebine in oblike ostane |
| **Prijave na novičnik** | ponudnik e-pošte (npr. Mailchimp, Brevo) – obrazec poveži z njihovim vgrajenim obrazcem | v Artifactu prijava ne more delovati |

Pred objavo na lastni domeni dodaj `og:` metapodatke, `canonical`, favicon in stran 404.

## 7. Pravne obveznosti v Sloveniji (preveri za vsak projekt)

- **Piškotki:** neobvezni piškotki (analitika, oglasi, vgrajeni videi) le s predhodno privolitvijo (ZEKom-2, smernice Informacijskega pooblaščenca). Brez analitike pasica ni potrebna.
- **Varstvo osebnih podatkov (GDPR, ZVOP-2):** pri obrazcih (novičnik, prijava) politika zasebnosti, namen, upravljavec, rok hrambe; potrditev prijave (double opt-in).
- **Dostopnost:** javni sektor (npr. AZN) mora izpolnjevati zahteve Zakona o dostopnosti spletišč in mobilnih aplikacij (ZDSMA, standard EN 301 549 / WCAG 2.1 AA) in objaviti izjavo o dostopnosti. Od 28. 6. 2025 velja tudi evropski akt o dostopnosti (EAA), ki ga prenaša slovenski zakon o zahtevah glede dostopnosti izdelkov in storitev; zajema določene zasebne storitve (npr. e-trgovina, bančne storitve). Ali stran spada mednje, preveri v vsakem projektu.
- **Mediji:** spletna publikacija z uredniško vsebino (npr. Uspešna Slovenija) je lahko medij po ZMed in mora biti vpisana v razvid medijev pri ministrstvu za kulturo, z odgovornim urednikom in kolofonom. Za pravno presojo uporabi skill `pravni-pregled-komunikacije-digitalne-storitve`.
- **Oglasi in partnerji:** plačane vsebine jasno označi (»Partner«, »Oglasno sporočilo«).

Te točke so opomnik, ne pravno mnenje. Pri objavi za naročnika jih uporabniku naštej kot seznam za preverjanje.

## 8. Kaj vrneš uporabniku

1. Povezavo do strani (Artifact) in pot do datoteke v repozitoriju.
2. Kratko: katero postavitev si izbral, kaj je prevzeto iz vzorca in kje si odstopil od pravil znamke.
3. Seznam manjkajočih vsebin in podatkov za preverjanje.
4. Naslednji korak do prave objave (domena, gostovanje, obrazci, pravne točke).

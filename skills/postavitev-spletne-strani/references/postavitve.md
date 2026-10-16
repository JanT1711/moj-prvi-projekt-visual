# Katalog postavitev – mere in ogrodja

Vse mere so za namizje (1280–1440 px); prelomi: 1060 px (tablica) in 720 px (telefon). Barve vedno iz skilla znamke prek CSS spremenljivk (`--paper`, `--ink`, `--muted`, `--rule`, `--accent`, `--kicker`).

## 1. Časopisna prva stran (po vzoru FT)

**Glava**
- Mreža `1fr auto 1fr`: levo ikoni meni in iskanje (40 × 40 px), sredina logotip (višina 56–64 px) z drobnim podnapisom v velikih črkah (11 px, razmik 0,16 em), desno temen gumb (novičnik, naročnina) in tekstovna povezava.
- Iskanje se odpre pod glavo kot polje s spodnjo črto 2 px in sproti filtrira novice.

**Vrstica rubrik**
- Med dvema črtama 1 px, rubrike v velikih črkah, 13–14 px, krepko, razmik 22 px.
- Izbrana rubrika: barva poudarka + spodnja črta 4 px.

**Prva stran – trije stolpci**
```css
.prva{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1.45fr) minmax(0,.8fr)}
.prva>*{padding-inline:22px;min-width:0}
.prva>*+*{border-left:1px solid var(--rule)}
```
- **Levo – vodilna:** nadnaslov (17 px, barva `--kicker`), naslov v serifu `clamp(34px,3.5vw,52px)` / 1.06, uvod 18 px `--muted`, oznaka (chip) z vrsto vsebine; spodaj ločena črta in še en naslov 21 px z datumom.
- **Sredina – slika:** 16:9, pod njo ploskev `--panel` s centriranim nadnaslovom in naslovom v serifu `clamp(24px,2.4vw,34px)`.
- **Desno – izbor:** naslov razdelka v barvi poudarka (»Izbor urednika«, »Pogled regulatorja«), 2–3 mnenjski naslovi 24 px z narekovajem v barvi poudarka in podpisom (krog 36 px + ime ali vir).

**Pod prvo stranjo**
- Trak 3–4 naslovov, nad njim debela črta 2 px `--ink`, med stolpci tanke črte.
- Razdelki po rubrikah: glava razdelka z debelo črto, naslovom 26 px in opisom desno; seznam naslov | datum.
- Stranski stolpec 300 px: novičnik, dogodek, pojasnilo.

**Telefon:** slika na vrh (`order:-1`), vse v en stolpec, navpične črte postanejo vodoravne, logotip levo, meni v vrstici rubrik.

**Tipografija:** naslovi `Source Serif 4` 600 (Google Fonts) ali Georgia; rubrike, oznake, besedilo v sansu znamke.

## 2. Mnenjska publikacija (Uspešna Slovenija)

- Glava: logotip levo, opis in prijava desno, pod tem ime publikacije v serifu `clamp(40px,6.4vw,68px)` in obljuba.
- Vodilni prispevek: slika 21:9 čez širino, naslov levo (1.75fr), uvod desno (1fr).
- Par (2 stolpca) → pasica partnerja → misel (citat čez širino) → trojec iz arhiva → trak piscev → novičnik.
- Vse ločnice 1 px, brez kartic in senc. Celoten CSS: `uspesna-slovenija-splet/references/osnovni.css`.

## 3. Institucionalne novice

- Bela stran, glava z logotipom levo in rubrikami spodaj.
- Grafitni pas z vodilno novico in abstraktnim motivom znamke.
- Dva stolpca: seznam novic (datum | nadnaslov, naslov, uvod, oznaka publike) s filtri »Vse / Širša / Strokovna« in stranski stolpec 320 px (novičnik, dogodek, »kaj počnemo in česa ne«).
- Na strani novice: ključne točke, okvir »Pogled regulatorja« ali »Kaj to pomeni za vas«, vir, povezava na izvirnik.

## 4. Pristajalna stran (dogodek, kampanja)

1. Uvodni pas: ime dogodka, datum in kraj (velike številke), en gumb (»Prijava«).
2. Zakaj priti: 3 trditve s kratko razlago.
3. Program po urah (tabela s tabelaričnimi števkami).
4. Govorci: mreža portretov (krog ali 4:5) z imenom in funkcijo.
5. Prijavni obrazec ali povezava na sistem za prijave.
6. Pogosta vprašanja (`details/summary`).
7. Partnerji (logotipi v sivi ali enobarvni različici), noga.

## 5. Predstavitev projekta / ponudba za partnerje

1. Teza v enem stavku in podnaslov.
2. Doseg v številkah (3–4 podatki z virom).
3. Paketi v tabeli (stolpci = paketi, vrstice = ugodnosti), priporočeni paket označen.
4. Reference in citati partnerjev (le resnični, z dovoljenjem).
5. Časovnica in kontakt (naslov kot besedilo, ki ga je mogoče kopirati).

## Skupna pravila za vse postavitve

- Črte namesto kartic, kjer je vsebine veliko; kartice le za element, ki mora izstopati.
- En poudarek barve na znamko; semantične barve (napaka, uspeh) ločeno.
- Naslovi s `text-wrap: balance`, besedilo do ~70 znakov v vrstici.
- Prazna mesta za slike in logotipe partnerjev s črtkanim robom in mero (npr. »970 × 250«).

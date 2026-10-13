---
name: "uspesna-slovenija-splet"
description: "Spletna publikacija Uspešna Slovenija (SBC – Klub slovenskih podjetnikov): oblikovni sistem, predloge strani (naslovnica, prispevek, tema, arhiv, pisci), komponente, vsebinski model in uredniška pravila za splet. Uporabi pri vsaki spletni strani, pristajalni strani, novičniku ali HTML predlogi za Uspešno Slovenijo ali za SBC-jev spletni mnenjski portal, tudi če uporabnik reče samo »stran«, »portal« ali »spletna izdaja«."
---

# Uspešna Slovenija – spletna publikacija

Mnenjska spletna publikacija SBC – Kluba slovenskih podjetnikov: »Ideje za državo, v kateri želimo ustvarjati, delati in živeti.« Pravila so izluščena iz vzorca »Vzorec B« (po Gregorjevem predlogu, nova številka in arhiv 1/2026). Vrednosti so natančne, vzete iz izvirnega CSS.

**Slog v enem stavku:** topel papir, Georgia v navadni debelini, tanke sive ločnice in temnozelen nadnaslov – tipografija nosi stran, fotografije so samo pri prispevkih in piscih.

**Razmerje do drugih skillov:**
- Spletna publikacija je **namerno drugačna od tiskane revije SBC** (`oblikovalec-sbc`, `sbc-revija-slog`): ni rumene, ni Special Elite, ni inicialke na zvezdi. Teh elementov ne prenašaj na splet, razen če uporabnik to izrecno želi.
- Za splošna pravila spletnih strani (dostopnost, odzivnost, SEO, preizkus) uporabi še `spletne-strani`.
- Za besedila `urednik-sbc` in `urednik-novinar-copywriter`, za vsebino `podjetnisko-okolje-slovenija` in `ekonomisti-slovenski-prostor`.

## 1. Barve

| Žeton | HEX | Vloga |
|---|---|---|
| `--paper` | `#F7F4ED` | ozadje strani (topel papir) |
| `--ink` | `#202620` | besedilo, naslovi, debela ločnica nad razdelki |
| `--muted` | `#5C645B` | uvodi, datumi, opisi, navigacija |
| `--rule` | `#C8C8BA` | tanke ločnice, robovi polj, črtkani robovi mest za partnerje |
| `--green` | `#314A35` | edini poudarek: nadnaslovi (kicker), povezave »→«, gumbi, citati, fokus |
| `--wash` | `#E9EDE3` | ploskve: novičnik, okvir »O avtorju«, opomba, monogram |
| `--card` | `#FBFAF6` | polja obrazcev, mesta za partnerje |
| svetlo besedilo na zeleni | `#F1EEE7` | besedilo na gumbih in zelenem pasu |

- Ena barva poudarka (zelena). Druge barve prihajajo le iz fotografij, ki so rahlo umirjene: `filter: saturate(.82) contrast(1.02)`.
- Portreti v krogu so črno-beli: `filter: grayscale(1) contrast(1.05)`.
- Kontrast: `--muted` na `--paper` je ≈ 5,6 : 1 (AA za navadno besedilo). Svetlejše sive za besedilo ne uvajaj.

## 2. Pisave

| Vloga | Pisava | Opomba |
|---|---|---|
| Naslovi, uvodi, telo prispevka, citati, imena piscev, številke | `Georgia, "Times New Roman", serif` | **vedno teža 400**, tudi v naslovih |
| Navigacija, nadnaslovi, podpisi, datumi, gumbi, obrazci, noga | `Arial, Helvetica, sans-serif` | krepko (700) le za podpis in kicker |

Sistemski pisavi – brez spletnih pisav, brez `@font-face`, hitro nalaganje. Ne zamenjuj ju z Google Fonts brez razloga.

## 3. Tipografska lestvica

| Element | Pisava | Velikost / razmik | Letter-spacing | Drugo |
|---|---|---|---|---|
| Ime publikacije `.naslov` | serif | `clamp(40px, 6.4vw, 68px)` / 1.05 | −0,045 em | »Uspešna Slovenija.« s piko |
| Naslov prispevka (stran) | serif | `clamp(34px, 5vw, 52px)` / 1.08 | −0,035 em | |
| Glava seznama (Tema, Arhiv, Pisci) | serif | `clamp(38px, 5.4vw, 56px)` / 1.05 | −0,04 em | spodaj 1 px `--ink` |
| Vodilni prispevek | serif | `clamp(28px, 3.9vw, 42px)` / 1.12 | −0,025 em | |
| Misel (citat na naslovnici) | serif | `clamp(25px, 3.3vw, 36px)` / 1.22 | −0,02 em | |
| Citat v prispevku | serif, zelen | `clamp(23px, 2.8vw, 28px)` / 1.32 | −0,015 em | levi rob 2 px zelen |
| Seznam / par / trojec | serif | 27 / 25 / 22 px | −0,02 em | |
| Telo prispevka `.besedilo` | serif | 19 px / 1.72 (telefon 18 px) | | razmik odstavkov 22 px |
| Uvod `.intro` | serif, `--muted` | 17 px / 1.65 (na strani prispevka 20 px / 1.55) | | |
| Kicker | sans 700, velike črke, zelen | 11 px / 1.45 | 0,14 em | |
| Podpis `.byline` | sans 700 | 12–13 px / 1.4 | | datum za `·` v 400 `--muted` |
| Navigacija | sans, `--muted` | 12 px | | aktivna: `--ink`, 700 |
| Gumb | sans 700, velike črke | 12 px / 1 | 0,1 em | ravni robovi (`border-radius:0`) |
| Napis pod sliko, oznaka »Partner« | sans | 10–11 px | 0,14 em (oznaka) | |

Vsi naslovi imajo `text-wrap: balance`. Lebdenje na naslovu: podčrtaj (`text-underline-offset:5px`, barva `--rule`).

## 4. Mreža in prostor

- Vsebina: `max-width: 1040px`, robovi 34 px (telefon 20 px). Prispevek: stolpec `max-width: 720px` na sredini.
- Prelom za telefon: **760 px** – vse mreže v en stolpec, navpične ločnice postanejo vodoravne.
- Ločnice namesto kartic: 1 px `--rule` med stolpci in vrsticami; 1 px `--ink` nad pomembnim razdelkom (misel, vprašanja, model, podatki, glava seznama). Brez senc in zaobljenih vogalov (razen krogov za portrete).
- Mreže: vodilni `1.75fr 1fr` (naslov | uvod, poravnano spodaj), par `1fr 1fr`, trojec `repeat(3,1fr)` z notranjim razmikom 26 px, seznam `150px 1fr 220px`, arhiv `150px 1fr`.
- Razmerja slik: vodilna 21:9 (telefon 16:10), ostale 16:10, `object-fit:cover`.

## 5. Komponente

Celoten CSS je v `references/osnovni.css`, delujoča enostranska predloga v `references/predloga.html`. Ključni deli:

**Glava** – logotip SBC (168 px, telefon 145 px) levo; desno opis »POGLEDI NA NAŠO PRIHODNOST« (11 px, velike črke, 0,13 em) in povezava »Prijava« (zelena, podčrtana s 1 px). Pod tem ime publikacije, obljuba (15 px, `--muted`) in navigacija tem med dvema ločnicama: V ospredju · Gospodarstvo · Država · Tehnologija · Zdravstvo · Ljudje · Arhiv · Pisci.

**Kicker + naslov + podpis** – osnovna enota vsakega prispevka:
```html
<span class="kicker">Strateški pogled</span>
<h2><a href="#tehnoloski-prelom">Če Slovenija zamudi tehnološki prelom, lahko izpade iz igre</a></h2>
<p class="byline">dr. Egon Zakrajšek <span>· 29. 8. 2026</span></p>
```
Kicker je **zvrst ali kot pogleda** (Strateški pogled, Kolumna, Esej, Pogovor, Tehnološki preboj), ne nujno ime teme.

**Misel** – en citat iz arhiva čez širino, `border-top:1px solid var(--ink)`, desno avtor in povezava »Preberi esej«. Citat v slovenskih narekovajih »…«.

**Razdelek** – naslov (serif 24 px) levo, kratek opis ali »Vsi pisci →« desno, spodaj ločnica.

**Pisci** – krog 52 px (na strani pisca 84 px, v okvirju O avtorju 72 px): fotografija črno-bela ali **monogram** (inicialke v serifu, zelene na `--wash`), ko fotografije ni.

**Novičnik** – ploskev `--wash`: »Tri razmišljanja. Vsak drugi teden.« + polje e-pošte (brez desnega roba) + zelen gumb »Prijava«. Odziv v `aria-live="polite"`.

**Citat v prispevku** – `<blockquote>` z levim zelenim robom 2 px, besedilo zeleno.

**Model** (npr. Glava · Srce · Roka) – trije stolpci, ključna beseda v serifu 25 px, razlaga v sans 14 px `--muted`.

**Podatki** – seznam `<dl>`: velika številka v serifu 28 px s tabelaričnimi števkami, opis desno, vir pod seznamom (11 px).

**Na kaj odgovarja ta prispevek** – 3 vprašanja v `<details>` (prvo odprto), znak +/−. Odgovori dobesedno iz besedila. Služi bralcem in iskalnikom (FAQ, odgovori za AI-iskanje).

**O avtorju** – ploskev `--wash`, krog 72 px, ime, vloga, »Vsa besedila avtorja →«.

**Partnerji** (uredniško ločeni od vsebine):
- `partner-glava` – »PUBLIKACIJO OMOGOČA« + mesto za logotip 132 × 34 px pod navigacijo;
- `oglas` – oznaka »PARTNER« in pasica **970 × 250** (telefon **320 × 100**);
- `omogoca` – pod prispevkom: »Ta prispevek omogoča … Partnerji podpirajo izhajanje Uspešne Slovenije. Na vsebino prispevkov ne vplivajo.«
Na naslovnici največ ena pasica, na strani prispevka nobene v besedilu.

**Noga** – logotip 130 px, stavek »Uspešna Slovenija je publikacija SBC – Kluba slovenskih podjetnikov. Avtorji pišejo v svojem imenu.«, povezave Pisci · Arhiv · Prijava na novičnik · sbc.si in trak ključnih številk SBC (številka v serifu 17 px + oznaka 12 px).

## 6. Predloge strani

1. **Naslovnica:** glava → partner → vodilna slika 21:9 z napisom (»Ilustracija: AI« / »Foto: …«) → vodilni prispevek (naslov levo, uvod desno) → par dveh prispevkov → pasica → misel → »Znova preberi« (trojec iz arhiva z uvodom in datumom) → trak piscev → novičnik → noga.
2. **Prispevek:** kicker, h1, uvod 20 px, podpisna vrstica med ločnicama (krog, ime, »Tema · datum«, gumb »Kopiraj povezavo«), slika z napisom, besedilo (odstavki, mednaslovi h2 26 px, citati, model, podatki), »Na kaj odgovarja ta prispevek«, O avtorju, »Ta prispevek omogoča«, »Preberi še« (3 prispevki, najprej ista tema), novičnik.
3. **Tema:** glava seznama (ime + opis teme) → seznam: izdaja in datum | kicker, naslov, uvod, avtor | slika → »Nova razmišljanja na to temo se dodajo na vrh seznama.« → pasica.
4. **Arhiv:** po številkah (»Številka 1/2026«, datum) s seznamom prispevkov; vsak ima stalno povezavo.
5. **Pisci:** mreža 3 × n: krog 84 px, ime, vloga, seznam prispevkov s temo in datumom.

## 7. Vsebinski model

Stran se izriše iz podatkov (glej `predloga.html`); novo vsebino dodaš z vnosom, ne s prerisovanjem HTML.

```js
TEME   = { tehnologija:{ ime, opis }, … }               // Gospodarstvo, Država, Tehnologija, Zdravstvo, Ljudje
IZDAJE = { "1-2026":{ ime:"Številka 1/2026", datum:"29. 8. 2026", iso:"2026-08-29" } }
PISCI  = { burger:{ ime:"dr. Anže Burger", vloga, foto?, inicialke? } }
CLANKI = { "slug":{ izdaja, tema, kicker, pisec, naslov, intro?, slika, foto,
                     besedilo:[["p",…],["q",…],["h",…],["model"],["podatki"]], vprasanja:[[v,o],…] } }
```
Pot je `#slug` (prispevek), `#tema`, `#arhiv`, `#pisci`, `#novicnik`. Naslov zavihka: »Naslov | Uspešna Slovenija«.

## 8. Uredniška pravila za splet

- **Naslov** je teza ali poziv v polnem stavku (»Nehajmo iskati razloge, zakaj pri nas nečesa ne moremo«), brez velikih črk in brez poudarkov.
- **Uvod** 1–2 stavka, ki povesta spor ali številko (»Rast imamo, konkurenčnost izgubljamo.«).
- **Nazivi** pred imenom z malo: dr., prof. dr. Datum `29. 8. 2026` (presledki za pikami).
- **Citati** v »…«; izpostavljeni citat je dobeseden stavek iz besedila.
- **Vprašanja na koncu** so vprašanja, ki bi jih bralec vpisal v iskalnik; odgovor iz avtorjevih besed.
- **Napis pod sliko** vedno: »Ilustracija: AI« ali »Foto: Ime Priimek/Agencija«. Za neznanega avtorja `[avtor fotografije]` – ne izmišljuj.
- **Ločitev partnerjev**: vsaka plačana vsebina ima oznako »Partner« in stavek, da partnerji ne vplivajo na vsebino.
- Mesta za manjkajoče podatke označi z oglatimi oklepaji (`[kratka predstavitev avtorja]`, `[datum izida]`) in jih naštej uporabniku.

## 9. Postopek in kontrolni seznam

1. Ugotovi vrsto strani (naslovnica, prispevek, tema, arhiv, pisci, pristajalna stran, e-novičnik).
2. Zberi vsebino v vsebinski model; manjkajoče označi.
3. Začni iz `references/predloga.html` in `osnovni.css`, ne iz nič.
4. Preveri:
   - [ ] samo zelena kot poudarek, brez rumene in brez Special Elite;
   - [ ] Georgia 400 za naslove in telo, Arial za oznake;
   - [ ] ločnice namesto kartic, brez senc in zaobljenih robov;
   - [ ] vsak prispevek ima kicker, naslov, avtorja in datum; slika ima napis;
   - [ ] partnerji označeni in ločeni od vsebine;
   - [ ] na 390 px ni vodoravnega drsenja, mreže so v enem stolpcu;
   - [ ] fokus je viden (zelen obris 2 px), slike imajo `alt` ali `alt=""`, če so okrasne;
   - [ ] množina pri številu prispevkov: 1 prispevek, 2 prispevka, 3–4 prispevki, 5+ prispevkov.
5. Upodobi stran (namizje 1440 px in telefon 390 px) in jo preglej, preden jo oddaš.

## Sredstva in omejitve

- Logotip SBC (`img/sbc-logo.svg`) v vzorcu ni bil objavljen. Uporabljaj le datoteko, ki jo da uporabnik; ne riši ga na novo. Do takrat besedilo »SBC – Klub slovenskih podjetnikov« v sans 12 px.
- Fotografije piscev in ilustracije (`img/*.jpg`) v vzorcu manjkajo; zahtevaj jih ali uporabi monograme in ploskve `--wash`.
- Številke v nogi (412 uspešnih podjetij, 23.000+ delovnih mest, 3,1 mrd € skupnega kapitala) so iz vzorca – pred objavo jih potrdi pri SBC.
- Imena, naslovi in citati iz vzorca so primeri, ne vsebina za nove strani.

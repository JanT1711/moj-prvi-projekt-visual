# Dopolnila obstoječih skillov

Spodnje bloke prilepi v obstoječe skille (claude.ai → Nastavitve → Skills → uredi). Novi skilli `uspesna-slovenija-splet` in `spletne-strani` so v tej mapi.

---

## 1. `oblikovalec-sbc` – zamenjaj alinejo »Spletna stran ali HTML« v razdelku 8

```markdown
- **Spletna stran ali HTML:**
  - Za spletno publikacijo **Uspešna Slovenija** uporabi skill `uspesna-slovenija-splet`. Ta ima namerno drug slog kot tiskana revija: topel papir `#F7F4ED`, temnozelen poudarek `#314A35`, Georgia 400 in Arial, tanke ločnice – brez rumene, brez Special Elite in brez inicialke na zvezdi.
  - Za druge spletne izdelke v slogu revije SBC uporabi spodnje žetone, za gradnjo, odzivnost in dostopnost pa skill `spletne-strani`.
```

Pod kontrolni seznam (razdelek 9) dodaj:

```markdown
9. Splet: je jasno, ali gre za revijo SBC (rumena, Special Elite) ali za Uspešno Slovenijo (zelena, Georgia)? Sloga ne mešaj.
```

---

## 2. `sbc-revija-slog` – na začetek razdelka 3 »Izvedba v HTML ali predlogi«

```markdown
> Za spletno publikacijo **Uspešna Slovenija** (mnenjski portal SBC) ne uporabljaj tega razdelka, ampak skill `uspesna-slovenija-splet`. Splošna pravila za spletne strani so v skillu `spletne-strani`.
```

V seznam rubrik (razdelek 2) dodaj alinejo:

```markdown
- Spletna publikacija Uspešna Slovenija: teme Gospodarstvo, Država, Tehnologija, Zdravstvo, Ljudje; zvrsti Strateški pogled, Kolumna, Esej, Pogovor, Tehnološki preboj (glej `uspesna-slovenija-splet`).
```

---

## 3. `urednik-sbc` – nov razdelek »Spletna izdaja Uspešna Slovenija«

```markdown
## Spletna izdaja Uspešna Slovenija

Ko pripravljaš besedilo za spletno publikacijo Uspešna Slovenija (oblikovanje: `uspesna-slovenija-splet`):

- **Kicker** = zvrst ali kot (Strateški pogled, Kolumna, Esej, Pogovor, Tehnološki preboj), največ dve besedi.
- **Naslov** = teza ali poziv v celem stavku, brez velikih črk in brez poudarkov (»Nehajmo iskati razloge, zakaj pri nas nečesa ne moremo«).
- **Uvod** = 1–2 stavka s sporom ali številko (»Rast imamo, konkurenčnost izgubljamo.«).
- **Izpostavljeni citati** = 2–4 dobesedni stavki iz besedila, v »…«.
- **Mednaslovi** = kratki, lahko vprašanje (»Kapital ali solidarnost?«), v navadnem zapisu – ne v velikih črkah kot v tiskani reviji.
- **»Na kaj odgovarja ta prispevek«** = 2–3 vprašanja, ki bi jih bralec vpisal v iskalnik, z odgovori iz avtorjevih besed.
- **O avtorju** = ena vrstica: funkcija, ustanova.
- **Napis pod sliko** = »Ilustracija: AI« ali »Foto: Ime Priimek/Agencija«.
- Za vsak prispevek oddaj tudi vnos za vsebinski model (`naslov`, `kicker`, `tema`, `pisec`, `intro`, `besedilo`, `vprasanja`).
- Avtorji pišejo v svojem imenu – ne pripisuj jim izjav, ki jih niso dali.
```

---

## 4. `oblikovalec` – v uvod dodaj

```markdown
Za spletne strani in HTML predloge uporabi še skill `spletne-strani` (gradnja, odzivnost, dostopnost, preizkus) in skill znamke (`uspesna-slovenija-splet`, `oblikovalec-sbc`, `the-adriatic-dizajn`, `azn-oblikovanje`).
```

---

## 5. `dizajn-iz-html` – v razdelek 1 »Upodobi izvirnik« dodaj

```markdown
Pri spletnih straneh (ne izvozih iz Claude Design) je CSS pogosto berljiv neposredno v `<style>`: najprej preberi `:root` spremenljivke in komentarje avtorja – to so natančne vrednosti. Upodobi tudi vse poti (`#…`) in telefonsko širino 390 px. Relativne slike (`img/…`) v objavljenih artifaktih pogosto manjkajo – zabeleži jih kot manjkajoča sredstva.
```

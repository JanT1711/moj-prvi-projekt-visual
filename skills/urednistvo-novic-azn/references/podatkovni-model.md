# Podatkovni model pulta Novice AZN

Vsi časi so UTC v zapisu ISO 8601 (`2026-10-16T10:00:00Z`), datumi objave `YYYY-MM-DD`. Id-ji: male črke, števke in `-`.

## clanki/<id> in objave/<id>

Isti nabor polj; `objave` ima še `objavljeno`.

| Polje | Tip | Opis |
|---|---|---|
| `naslov` | niz | obvezno |
| `uvod` | niz | 1–2 stavka, do 280 znakov |
| `tema` | niz | id iz `teme` |
| `publika` | `siroka` \| `strokovna` | prikaz: »Za zavarovance« / »Za stroko« |
| `datum` | `YYYY-MM-DD` | prikazani datum objave |
| `besedilo` | niz | prazna vrstica = odstavek, `## ` = medmastni naslov, `> ` = citat; lahko prazno |
| `tocke` | seznam nizov | ključne točke |
| `pogled` | niz | »Pogled regulatorja«; potreben za mesto v stolpcu na naslovnici |
| `zavas` | seznam nizov | »Kaj to pomeni za vas« |
| `vir` | niz | npr. »Povzetek stališča EIOPA.« |
| `url` | niz (https) | izvirnik na a-zn.si |
| `slika` | niz | id iz `fotografije` ali prazno |
| `alt` | niz | opis slike |
| `napisSlike` | niz | npr. »Foto: Ime Priimek« |
| `posodobljeno` | čas | zadnja shranitev |
| `ustvarjeno` | čas | prva shranitev |
| `posodobil` | id osebe ali null | iz `user.id()`; imen ne shranjuj |
| `objavljeno` | čas | samo v `objave` |

## stran/naslovnica

```json
{"obvestilo": "", "vodilna": "<id>", "druga": "<id>", "slika": "<id>",
 "izbor": ["<id>", "<id>"], "trak": ["", "", ""], "posodobljeno": "…", "posodobil": null}
```
Prazen niz = samodejno. Stran preskoči id-je, ki niso v `objave`, in ne pokaže istega članka dvakrat (razen v stolpcu »Pogled regulatorja«).

## teme/<slug>
`{"ime": "Dolgoživost", "opis": "…", "red": 1}`

## povezave/<id>
`{"oznaka": "a-zn.si", "url": "https://www.a-zn.si/", "mesto": "oba", "red": 1}` – `mesto`: `glava`, `noga` ali `oba`.

## fotografije/<id>
`{"asset": "<32-znakovni id iz shrambe>", "opis": "…", "vir": "Foto: …", "ustvarjeno": "…", "nalozil": null, "velikost": 123456}`
Slika se prikaže z `"/_blob/" + asset`. Fotografije, ki jo uporablja članek, pult ne dovoli izbrisati.

## Začetno stanje (16. 10. 2026)
Rubrike `dolgozivost`, `tveganja`, `nadzor`, `podatki`; povezava `a-zn`; pet objavljenih člankov: `dolgozivost-kako-dobro`, `ziveti-sto-let`, `nadzor-izvorni-podatki`, `messi-mbappe`, `konkurencnost-stabilnost`.

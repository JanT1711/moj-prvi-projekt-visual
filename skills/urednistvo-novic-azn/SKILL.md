---
name: "urednistvo-novic-azn"
description: "Uredniški pult (dashboard) za spletno stran Novice AZN: dodajanje, urejanje, objava in umik člankov, fotografije, naslovnica, rubrike in povezave – neposredno v bazi pulta ali z navodili uporabniku – ter nadgradnja kode pulta. Uporabi, ko uporabnik želi objaviti ali popraviti članek za Novice AZN, pretvoriti AZN-jev članek (docx, PDF, povezava a-zn.si) v objavo, spremeniti naslovnico, dodati fotografijo, rubriko ali povezavo, ali razširiti ali popraviti pult."
---

# Uredništvo Novic AZN

Pult je artefakt v claude.ai z dvema deloma v isti povezavi:
- **uredništvo** (`#pregled`, `#clanki`, `#uredi-<id>`, `#nov`, `#naslovnica`, `#fotografije`, `#povezave`) za urejevalce;
- **javna stran** (`#stran`, `#stran-<id>`, `#stran-rub-<rubrika>`) v časopisni postavitvi, ki prikazuje samo objavljene članke.

**Povezava:** https://claude.ai/artifact/GKUue8CK2feUqNnuEgv1Cj
**Izvorna koda:** `references/azn-urednistvo.src.html` (v repozitoriju `moj-prvi-projekt-visual` tudi `strani/azn-urednistvo.src.html`).

Videz in uredniška pravila prihajajo iz skilla `azn-oblikovanje`; postavitev javne strani je »časopisna prva stran« iz skilla `postavitev-spletne-strani`. Za besedila uporabi še `urednik-novinar-copywriter`.

## 1. Podatkovni model

Vse je v bazi artefakta (orodje `ArtifactData`, `url` = povezava zgoraj). Podrobnosti polj: `references/podatkovni-model.md`.

| Zbirka | Kaj | Kdo bere |
|---|---|---|
| `clanki/<id>` | vsi članki, tudi osnutki – delovna različica | samo `interact` in več (Contributor, Editor, lastnik) |
| `objave/<id>` | posnetek objavljene različice; javna stran bere samo to | vsi, ki odprejo povezavo |
| `stran/naslovnica` | razporeditev naslovnice in obvestilo na vrhu | vsi |
| `teme/<id>` | rubrike (meni), polje `red` = vrstni red | vsi |
| `povezave/<id>` | povezave v glavi/nogi (`mesto`: glava, noga, oba) | vsi |
| `fotografije/<id>` | opis in vir slike + `asset` (id v shrambi artefakta) | vsi |

Pravilo dostopa (ob objavi kode): `db: {rules: [{path: "clanki", read: "interact", write: "interact"}]}`, poleg tega `user: {}` in `assets: {}`. Ob ponovni objavi kode `capabilities` izpusti, da ostanejo nespremenjene.

**Stanje članka** se izračuna: ni v `objave` → *osnutek*; `clanki.posodobljeno` > `objave.objavljeno` → *neobjavljene spremembe*; sicer *objavljeno*.

## 2. Delo z vsebino prek baze (ko uporabnik prosi Claude)

Vedno najprej preberi (`get`/`list`) in piši z `if_version`; več zapisov združi v en `batch`.

**Nov članek iz AZN-jevega besedila (docx, PDF, a-zn.si):**
1. Preberi izvirnik v celoti (`pandoc x.docx -t plain`, skill `pdf`). Ne povzemaj po spominu.
2. Izpolni polja po hišnem slogu AZN (`azn-oblikovanje/references/azn-clanki-slog.md`):
   - `naslov` – vprašanje ali kontrastna trditev iz izvirnika;
   - `uvod` – 1–2 stavka, največ 280 znakov;
   - `tema` – obstoječi `teme/<id>`; če nobena ne ustreza, predlagaj novo, ne ustvarjaj je brez vprašanja;
   - `publika` – `siroka` ali `strokovna`;
   - `besedilo` – celotno besedilo (prazna vrstica = odstavek, `## ` = medmastni naslov, `> ` = citat) ali prazno, če stran le povzema;
   - `tocke` – 3–5 ključnih točk, dobesedno zveste izvirniku;
   - `pogled` – le če izvirnik vsebuje stališče AZN ali povzeto stališče (EIOPA, IAIS) z navedbo vira;
   - `zavas` – le splošni nasveti; nikoli priporočila zavarovalnic ali nasvet posamezniku;
   - `vir`, `url` (https, a-zn.si), `datum` (ISO `YYYY-MM-DD`).
3. `id` = slug naslova brez šumnikov + kratka pripona (npr. `zavarovanje-toce-k3f9`).
4. Zapiši `clanki/<id>` s `posodobljeno` = zdaj (UTC ISO) in `ustvarjeno`. **Ne objavljaj sam** – osnutek pokaži uporabniku in vprašaj.
5. Ob potrditvi objave: `objave/<id>` = enaka vsebina + `objavljeno` = zdaj (vsaj sekundo za `posodobljeno`).

**Popravek objavljenega članka:** popravi `clanki/<id>` (nov `posodobljeno`), nato po potrditvi prepiši `objave/<id>` z novim `objavljeno`. Le popravek v `clanki` pusti na strani staro različico.

**Umik:** izbriši `objave/<id>`; `clanki/<id>` ostane kot osnutek. **Brisanje** obeh le na izrecno zahtevo.

**Naslovnica:** `stran/naslovnica` = `{obvestilo, vodilna, druga, slika, izbor:[id,id], trak:[id,id,id]}`; prazen niz = samodejno (najnovejše objave). Mesta `izbor` sprejmejo le članke z izpolnjenim `pogled`. Vsak id mora biti v `objave`.

**Fotografija:** naloži datoteko z orodjem `Artifact` (`url` pulta, `file_path`, `asset: true`) in iz rezultata vzemi `id`; nato zapiši `fotografije/f-<prvih 12 znakov id>` = `{asset: <id>, opis, vir, ustvarjeno}` in v članku nastavi `slika`, `alt`, `napisSlike`. Brez fotografij znanih oseb in logotipov tretjih; dekorativna slika ima alt »Dekorativna slika.«.

**Rubrike in povezave:** `teme/<slug>` = `{ime, opis, red}`; `povezave/<id>` = `{oznaka, url (https), mesto, red}`. Rubrike, ki jo uporablja kak članek, ne briši.

## 3. Navodila uporabniku (ko dela sam v pultu)

- Nov članek: *Članki → + Nov članek* → izpolni → *Shrani osnutek* → *Objavi*.
- Popravek: *Uredi* → *Posodobi objavo* (rumena značka »Neobjavljene spremembe« opozori, da popravek še ni na strani).
- Fotografije nalagajo **Editorji**; Contributorji izbirajo med naloženimi.
- Dostop se ureja v meniju *Share*: Viewer = samo javna stran, Contributor = urejanje člankov, Editor = tudi fotografije in koda.

## 4. Pred vsako objavo preveri

1. Številke, letnice in citati se ujemajo z izvirnikom; zastareli podatki (roki, deleži) so označeni uporabniku.
2. Nobena zavarovalnica ni izpostavljena ali priporočena.
3. Ni osebnega svetovanja; pozivi so splošni (»preberite pogoje«, »več na a-zn.si«).
4. Šumniki, datum, rubrika in publika so pravilni.
5. Fotografija ima alt in vir.

## 5. Nadgradnja kode pulta

1. Uredi `references/azn-urednistvo.src.html` (ali `strani/azn-urednistvo.src.html` v repozitoriju).
2. Zgradi: `python3 scripts/zgradi.py azn-urednistvo.src.html <azn-oblikovanje>/assets/logo azn-urednistvo.html`.
3. Lokalni preizkus s Playwrightom in nadomestnim `window.claude` (pomnilniška baza z `doc/collection/onSnapshot/set/update/delete`), 1440 px in 390 px, svetlo in temno, brez `pageerror` in brez vodoravnega drsenja.
4. Objavi na isto povezavo (`Artifact` z `url` ali isto pot datoteke) **brez** `capabilities`; če dodaš novo zbirko z drugačnimi pravicami, pošlji celoten nabor `capabilities` z vsemi pravili.
5. Pravila kode: vsako vrednost iz baze izpiši skozi `esc()`; naročila (`onSnapshot`) samo enkrat ob zagonu; zapis le ob dejanju uporabnika, vsak zapis počaka (`await`) na prejšnjega; brisanje vedno z dvostopenjsko potrditvijo v strani (`confirm()` ne deluje).

## 6. Omejitve in naslednji koraki

- Ni zgodovine različic in časovne objave; datum je le prikazan.
- Opozorilo o neshranjenih spremembah pride šele po odhodu iz urejevalnika.
- Javna stran je v claude.ai (bralci morajo imeti povezavo in biti prijavljeni). Za a-zn.si: izvoz `objave` (JSON) v CMS spletišča ali statično generiranje strani (glej `postavitev-spletne-strani`, razdelek Objava).
- Možne nadgradnje: pregled in odobritev (stanje »v pregledu«), načrtovana objava, izvoz za novičnik, karusel iz članka (skill `azn-oblikovanje`).

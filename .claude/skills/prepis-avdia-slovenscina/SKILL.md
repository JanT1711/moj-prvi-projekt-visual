---
name: "prepis-avdia-slovenscina"
description: "Prepis zvočnih in video posnetkov v slovensko besedilo z lektorskim pregledom: strojni prepis (Whisper), nato pregled strokovnjaka za slovenski jezik (lektor, redaktor, korektor, jezikoslovec), ki popravi napake razpoznave, imena, ločila in pravopis. Ravni: dobesedni, berljivi ali uredniški prepis; govorci, časovne oznake, podnapisi SRT, lektorski zapisnik. Uporabi pri vsakem posnetku, intervjuju, sestanku, podkastu, predavanju ali narekovanju v slovenščini in kadar uporabnik priloži strojni prepis, ki ga je treba urediti."
---

# Prepis avdia v slovensko besedilo

Postopek ima dva koraka: **strojni prepis** (razpoznava govora) in **lektorski pregled** po promptu strokovnjaka za slovenski jezik v `references/prompt-lektor.md`. Claude sam zvoka ne sliši – besedilo dobi iz razpoznavalnika, nato ga strokovno uredi.

Povezani skilli: `urednik-novinar-copywriter` (članek iz prepisa), `urednik-sbc` (intervju za revijo SBC), `video-producent` (podnapisi in montaža), `docs` ali `docx` (oddaja dokumenta).

## 1. Pred začetkom vprašaj (le, česar ni v pogovoru)

1. **Raven prepisa:** *dobesedni* (vse, tudi mašila – za raziskave, sodne in uradne zapise), *berljivi* (privzeto – brez mašil in zatikanj, knjižne oblike) ali *uredniški* (za objavo kot intervju ali članek).
2. **Govorci:** imena in vloge (npr. voditeljica, gost), število.
3. **Imena in izrazi**, ki se pojavijo (osebe, podjetja, ustanove, kratice, strokovni izrazi) – izboljšajo razpoznavo in pregled.
4. **Izdelek:** besedilo, dokument (Docs/Word), podnapisi SRT, osnova za članek.

## 2. Strojni prepis

**V tem okolju (Claude Code):**
```bash
pip install faster-whisper            # enkrat; ffmpeg je že nameščen
python3 scripts/prepisi.py posnetek.m4a --izhod prepis --imena "AZN, EIOPA, dr. Ana Novak"
```
- Model `large-v3` je najnatančnejši za slovenščino; na procesorju je počasen (približno realni čas ali več). Za hiter osnutek `--model medium`. Pri dolgih posnetkih poženi v ozadju.
- Izdelki: `surovi.txt` (odseki s časi), `surovi.srt`, `surovi.json` (s seznamom negotovih besed za vsak odsek).
- Ob prvem zagonu se model prenese s **huggingface.co** (large-v3 ≈ 3 GB). V oblačnem okolju Claude Code mora biti ta domena dovoljena v nastavitvah omrežja okolja (Network access → Allowed domains: `huggingface.co`, `*.hf.co`); sicer povej uporabniku in predlagaj spodnje možnosti. `--model` sprejme tudi pot do lokalno shranjenega modela.

**Druge možnosti** (ko uporabnik prinese prepis sam):
- slovenski razpoznavalniki (npr. rešitve, razvite v projektu RSDO in na CLARIN.SI, ali komercialni ponudniki za slovenščino),
- vgrajeni prepisi v Teams, Zoom, Google Meet, Word (Narekuj/Prepiši), YouTube.
Prepis teh orodij obravnavaj enako: kot surovo gradivo za pregled.

**Ločevanje govorcev:** Whisper govorcev ne loči. Pri dveh govorcih jih določi iz vsebine (vprašanja/odgovori) in jih označi; kjer ni jasno, zapiši **Govorec 1/2** in mesto označi. Za zanesljivo ločevanje predlagaj orodje z diarizacijo (npr. pyannote) ali prepis iz Teams/Zooma, ki govorce že loči.

## 3. Lektorski pregled

1. Preberi `references/prompt-lektor.md` in ravnaj po njem kot strokovnjak za slovenski jezik.
2. Pregleduj po delih (pribl. 10–15 minut posnetka naenkrat), da nič ne izpade; ohrani časovne oznake.
3. Najprej popravi **napake razpoznave** (podobno zveneče besede, razbite in zlepljene besede, napačna imena), nato **skladnjo in ločila**, nato **raven** (mašila, pogovorne oblike) po izbrani ravni.
4. Negotova mesta iz `surovi.json` in vse, česar ne moreš preveriti, označi z [?] ali [nerazumljivo hh:mm:ss].
5. Pri uredniški ravni govorca ne spreminjaj v drugo osebo: ohrani njegov slog in pomen. Navedke za objavo mora avtorizirati govorec.

Hitri pregled najpogostejših napak: `references/pogoste-napake.md`.

## 4. Oddaja

```
# [Naslov ali opis posnetka]
Datum posnetka: … · Trajanje: … · Raven: berljivi prepis

[00:00:05] **Voditeljica:** …
[00:00:21] **dr. Ana Novak:** …

---
Lektorski zapisnik
- [00:07:12] »Kavšek [?]« – ime ni jasno slišno, potrdite.
- »izgleda« → »je videti« (kalk); v dobesednem navedku ohranjeno.
Odprta vprašanja: …
```
- Daljši prepis oddaj kot dokument (skill `docs`, ali `docx`, če želi Word), kratek neposredno v pogovoru.
- Podnapisi: popravljeno besedilo vrni v `surovi.srt` po istih časih (največ 2 vrstici po ~42 znakov na podnapis).

## 5. Kontrolni seznam

- [ ] Imena, nazivi, kratice, številke, zneski in datumi preverjeni ali označeni z [?].
- [ ] Ločila in velika začetnica po pravopisu; narekovaji »…«; pomišljaj –.
- [ ] Raven prepisa dosledna v celem besedilu.
- [ ] Pomen in slog govorca ohranjena; nič ni dodano ali izpuščeno (razen mašil pri berljivi ravni).
- [ ] Časovne oznake in govorci na mestu.
- [ ] Lektorski zapisnik z odprtimi vprašanji.

## Zasebnost

Posnetki pogosto vsebujejo osebne podatke. Datoteke obdelaj samo v tem okolju, ne pošiljaj jih v zunanje storitve brez uporabnikovega soglasja, in na koncu ponudi brisanje začasnih datotek.

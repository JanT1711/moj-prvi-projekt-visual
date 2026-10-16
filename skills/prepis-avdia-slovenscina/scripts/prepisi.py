#!/usr/bin/env python3
"""Strojni prepis slovenskega govora s faster-whisper (Whisper large-v3).

Namestitev (enkrat):  pip install faster-whisper
Uporaba:
  python3 prepisi.py posnetek.m4a --izhod mapa [--model large-v3] [--imena "AZN, EIOPA, dr. Ana Novak"]

Izdelki v mapi --izhod:
  surovi.txt   – odseki s časovnimi oznakami [hh:mm:ss] (vhod za lektorski pregled)
  surovi.srt   – podnapisi
  surovi.json  – odseki z besedami, časi in verjetnostmi (mesta z nizko verjetnostjo preveri)
"""
import argparse, json, os, subprocess, sys, tempfile


def cas(s, srt=False):
    h, r = divmod(s, 3600); m, r = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(r):02},{int((r % 1) * 1000):03}" if srt else f"{int(h):02}:{int(m):02}:{int(r):02}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("posnetek")
    p.add_argument("--izhod", default="prepis")
    p.add_argument("--model", default="large-v3", help="large-v3 (najboljši), medium, small (hitrejši)")
    p.add_argument("--imena", default="", help="lastna imena in izrazi, ki naj jih model pozna")
    p.add_argument("--naprava", default="auto", help="auto, cpu ali cuda")
    a = p.parse_args()

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("Manjka faster-whisper: pip install faster-whisper")

    os.makedirs(a.izhod, exist_ok=True)
    wav = os.path.join(tempfile.mkdtemp(), "vhod.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.posnetek, "-ac", "1", "-ar", "16000", wav], check=True)

    naprava = a.naprava
    if naprava == "auto":
        try:
            import ctranslate2
            naprava = "cuda" if ctranslate2.get_cuda_device_count() else "cpu"
        except Exception:
            naprava = "cpu"
    try:
        model = WhisperModel(a.model, device=naprava, compute_type="float16" if naprava == "cuda" else "int8")
    except Exception as e:
        sys.exit(f"Modela {a.model} ni mogoče naložiti ({type(e).__name__}). Ob prvem zagonu se prenese s huggingface.co – "
                 "če omrežje to blokira, dovolite domeno huggingface.co (in *.hf.co) ali podajte pot do lokalno shranjenega modela z --model.")

    uvod = "Prepis pogovora v slovenščini, z ločili in velikimi začetnicami."
    if a.imena:
        uvod += " Imena in izrazi: " + a.imena + "."
    odseki, info = model.transcribe(wav, language="sl", vad_filter=True, word_timestamps=True,
                                    beam_size=5, initial_prompt=uvod, condition_on_previous_text=True)

    vsi = []
    with open(os.path.join(a.izhod, "surovi.txt"), "w", encoding="utf-8") as txt, \
         open(os.path.join(a.izhod, "surovi.srt"), "w", encoding="utf-8") as srt:
        for i, s in enumerate(odseki, 1):
            besedilo = s.text.strip()
            txt.write(f"[{cas(s.start)}] {besedilo}\n")
            srt.write(f"{i}\n{cas(s.start, True)} --> {cas(s.end, True)}\n{besedilo}\n\n")
            vsi.append({"zacetek": round(s.start, 2), "konec": round(s.end, 2), "besedilo": besedilo,
                        "negotove": [w.word.strip() for w in (s.words or []) if w.probability < 0.5]})
            print(f"[{cas(s.start)}] {besedilo}", flush=True)
    json.dump({"trajanje": info.duration, "jezik": info.language, "odseki": vsi},
              open(os.path.join(a.izhod, "surovi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nKončano: {len(vsi)} odsekov, {cas(info.duration)}. Datoteke so v {a.izhod}/", file=sys.stderr)


if __name__ == "__main__":
    main()

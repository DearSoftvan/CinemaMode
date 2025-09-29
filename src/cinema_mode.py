import os
import json
import argparse
import subprocess

# Proje kök dizinini bul (src'nin bir üstü)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOLUME_STATE_FILE = os.path.join(BASE_DIR, "locales", "volume_state.json")

def load_language(lang="en"):
    """
    JSON dil dosyasını yükler.
    Eğer istenen dil bulunmazsa İngilizceye döner.
    """
    try:
        path = os.path.join(BASE_DIR, "locales", f"{lang}.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Language file not found, defaulting to English.")
        fallback = os.path.join(BASE_DIR, "locales", "en.json")
        with open(fallback, "r", encoding="utf-8") as f:
            return json.load(f)

def activate_cinema_mode(lang="en"):
    """
    Cinema Mode'u aktif eder.
    Şu anda örnek olarak ses çıkışını %50 yapar ve mesaj verir.
    """
    messages = load_language(lang)

    print(messages.get("starting", "Starting Cinema Mode..."))

    # Mevcut sesi oku ve kaydet
    try:
        result = subprocess.run(
            ["osascript", "-e", "output volume of (get volume settings)"],
            capture_output=True, text=True
        )
        current_volume = int(result.stdout.strip())
    except Exception:
        current_volume = 100

    try:
        with open(VOLUME_STATE_FILE, "w") as f:
            json.dump({"volume": current_volume}, f)
    except Exception:
        pass  # Dosya yazılamazsa sessizce geç

    # Cinema Mode sesi %50 yap
    try:
        subprocess.run([
            "osascript", "-e",
            'set volume output volume 50'
        ])
        print(messages.get("activate", "Cinema Mode activated!"))
        print(messages.get("tip", "Only the selected media app will play sound through your speakers."))
    except Exception as e:
        print(messages.get("error", "Error while activating Cinema Mode:"), e)

def deactivate_cinema_mode(lang="en"):
    """
    Cinema Mode'u devre dışı bırakır.
    Ses çıkışını önceki seviyeye veya %100'e geri çevirir ve mesaj verir.
    """
    messages = load_language(lang)

    print(messages.get("starting", "Deactivating Cinema Mode..."))

    # Önceki sesi oku
    try:
        if os.path.exists(VOLUME_STATE_FILE):
            with open(VOLUME_STATE_FILE, "r") as f:
                state = json.load(f)
            previous_volume = state.get("volume", 100)
        else:
            previous_volume = 100
    except Exception:
        previous_volume = 100

    try:
        subprocess.run([
            "osascript", "-e",
            f'set volume output volume {previous_volume}'
        ])
        print(messages.get("deactivate", "Cinema Mode deactivated!"))
    except Exception as e:
        print(messages.get("error", "Error while deactivating Cinema Mode:"), e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cinema Mode Utility")
    parser.add_argument("--lang", default="en", help="Language code (en, tr)")
    parser.add_argument("--deactivate", action="store_true", help="Deactivate Cinema Mode")
    args = parser.parse_args()

    if args.deactivate:
        deactivate_cinema_mode(args.lang)
    else:
        activate_cinema_mode(args.lang)

import os
import json
import argparse
import subprocess

# Proje kök dizinini bul (src'nin bir üstü)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

    try:
        # Örn: BlackHole ses aygıtını varsayılan yap
        subprocess.run([
            "osascript", "-e",
            'set volume output volume 50'
        ])
        print(messages.get("success", "Cinema Mode activated!"))
    except Exception as e:
        # Tek satır string kullanıldı, hata mesajı güvenli
        print(messages.get("error", "Error while activating Cinema Mode:"), e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cinema Mode Utility")
    parser.add_argument("--lang", default="en", help="Language code (en, tr)")
    args = parser.parse_args()

    activate_cinema_mode(args.lang)


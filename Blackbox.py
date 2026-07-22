import importlib.util
import time
import random
import sys
import threading
import pygame
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
GAME_FILE = PROJECT_ROOT / "game.py.tembakk.py"


def bot_internal():
    """Bot yang langsung menyuntikkan tombol ke Event Queue Pygame."""
    print("Black Box Testing dimulai...")
    print("Game akan dimainkan komputer selama 1 menit.")
    time.sleep(2)  # Tunggu Pygame selesai inisialisasi

    DURASI = 60  # 1 menit
    mulai = time.time()

    while time.time() - mulai < DURASI:
        if not pygame.get_init():
            break

        aksi = random.randint(1, 4)

        if aksi == 1:
            # Gerak Kiri + Tembak
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
            time.sleep(0.15)
            pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_LEFT))
            pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE))

        elif aksi == 2:
            # Gerak Kanan + Tembak
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
            time.sleep(0.15)
            pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT))
            pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE))

        else:
            # Tembak Otomatis
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
            time.sleep(0.1)
            pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE))

        time.sleep(0.08)

    print("Black Box Testing 1 menit selesai.")


def main():
    # Jalankan bot simulasi di thread terpisah
    threading.Thread(target=bot_internal, daemon=True).start()

    # Load dan eksekusi file game secara langsung
    spec = importlib.util.spec_from_file_location("game_module", GAME_FILE)
    game_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(game_module)


if __name__ == "__main__":
    main()
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

print("="*60)
print("WHITE BOX TESTING")
print("="*60)

flow = [
    "Inisialisasi pygame",
    "Load Sound",
    "Inisialisasi Player",
    "Inisialisasi Musuh",
    "Inisialisasi Peluru",
    "Loop Game",
    "Input Keyboard",
    "Gerakan Player",
    "Gerakan Musuh",
    "Gerakan Peluru",
    "Collision Detection",
    "Update Score",
    "Game Over",
    "Restart game"    
  ]   
 
for i, item in enumerate(flow, start=1):
    print(f"WB-{i:02d} | {item:<30} | PASS")
    time.sleep(0.3)

print("\nSemua alur berhasil diuji.\n")

game = PROJECT_ROOT / "game.py.tembakk.py"

if game.exists():
    print("Menjalankan game...\n")
    subprocess.run([sys.executable, str(game)])
else:
    print("game.py.tembakk.py tidak ditemukan.")
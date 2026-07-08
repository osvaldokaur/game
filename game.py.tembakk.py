import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Pengaturan Layar
LEBAR, TINGGI = 800, 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Game Tembak Bola - Space Edition")
jam = pygame.time.Clock()

# Warna
HITAM = (5, 5, 10)
PUTIH = (255, 255, 255)
MERAH_METEOR = (230, 50, 50)
ORANYE_EFEK = (255, 100, 0)
BIRU_UTAMA = (0, 140, 240)
BIRU_MUDA = (80, 200, 255)
KUNING_LASER = (255, 255, 100)
KUNING_GLOW = (255, 200, 0)

# Font
font_skor = pygame.font.SysFont("Arial", 35, bold=True)
font_game_over = pygame.font.SysFont("Arial", 70, bold=True)

# 1. Dekorasi Latar Belakang (Bintang-bintang kecil)
bintang_list = []
for _ in range(50):
    bintang_list.append([random.randint(0, LEBAR), random.randint(0, TINGGI), random.randint(1, 3)])

# 2. Karakter Pemain
pemain = pygame.Rect(375, 500, 50, 50)
kecepatan_pemain = 8

# 3. Struktur Banyak Musuh (Hujan Bola Merah)
UKURAN_MUSUH = 22
jumlah_musuh = 8
musuh_list = []
for _ in range(jumlah_musuh):
    rect_musuh = pygame.Rect(random.randint(0, LEBAR - UKURAN_MUSUH), random.randint(-400, -50), UKURAN_MUSUH, UKURAN_MUSUH)
    kecepatan = random.randint(3, 6)
    musuh_list.append({"rect": rect_musuh, "speed": kecepatan})

# 4. Peluru (Twin Laser)
peluru_list = []
kecepatan_peluru = 14
skor = 0

# Fungsi Menggambar Pesawat Karakter secara Detail
def gambar_pesawat(surface, x, y):
    warna_api = random.choice([BIRU_MUDA, PUTIH, BIRU_UTAMA])
    pygame.draw.polygon(surface, warna_api, [(x + 12, y + 48), (x + 16, y + 58), (x + 20, y + 48)])
    pygame.draw.polygon(surface, warna_api, [(x + 30, y + 48), (x + 34, y + 58), (x + 38, y + 48)])
    
    pygame.draw.rect(surface, BIRU_MUDA, (x, y + 30, 12, 18))
    pygame.draw.rect(surface, BIRU_UTAMA, (x + 4, y + 34, 4, 10))
    pygame.draw.rect(surface, BIRU_MUDA, (x + 38, y + 30, 12, 18))
    pygame.draw.rect(surface, BIRU_UTAMA, (x + 42, y + 34, 4, 10))
    
    pygame.draw.rect(surface, BIRU_UTAMA, (x + 12, y, 26, 48))
    pygame.draw.rect(surface, BIRU_MUDA, (x + 16, y, 18, 8))
    pygame.draw.rect(surface, PUTIH, (x + 20, y + 12, 10, 8))

# Loop Utama Game
running = True
while running:
    layar.fill(HITAM)
    
    # Menggambar & Menggerakkan Bintang Latar Belakang
    for bintang in bintang_list:
        bintang[1] += bintang[2] * 0.5
        if bintang[1] > TINGGI:
            bintang[1] = 0
            bintang[2] = random.randint(1, 3)
        pygame.draw.circle(layar, PUTIH, (bintang[0], int(bintang[1])), bintang[2])

    # 1. Input Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_kiri = pygame.Rect(pemain.x + 4, pemain.top + 10, 6, 20)
                laser_kanan = pygame.Rect(pemain.right - 10, pemain.top + 10, 6, 20)
                peluru_list.append(laser_kiri)
                peluru_list.append(laser_kanan)

    # 2. Pergerakan Pemain
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT] and pemain.left > 0:
        pemain.x -= kecepatan_pemain
    if tombol[pygame.K_RIGHT] and pemain.right < LEBAR:
        pemain.x += kecepatan_pemain

    # 3. Pergerakan Banyak Musuh
    for m in musuh_list:
        m["rect"].y += m["speed"]
        if m["rect"].y > TINGGI:
            m["rect"].y = random.randint(-150, -40)
            m["rect"].x = random.randint(0, LEBAR - UKURAN_MUSUH)
            m["speed"] = random.randint(3, 6)

    # 4. Pergerakan Peluru
    for peluru in peluru_list[:]:
        peluru.y -= kecepatan_peluru
        if peluru.bottom < 0:
            peluru_list.remove(peluru)

    # 5. Deteksi Tabrakan: Peluru vs Banyak Musuh
    for peluru in peluru_list[:]:
        hit_musuh = False
        for m in musuh_list:
            if peluru.colliderect(m["rect"]):
                skor += 1
                hit_musuh = True
                pygame.draw.circle(layar, ORANYE_EFEK, (m["rect"].centerx, m["rect"].centery), 30)
                m["rect"].y = random.randint(-200, -50)
                m["rect"].x = random.randint(0, LEBAR - UKURAN_MUSUH)
                m["speed"] = random.randint(3, 6)
                break
        if hit_musuh:
            peluru_list.remove(peluru)

    # 6. Menggambar Seluruh Objek Game
    for m in musuh_list:
        pygame.draw.circle(layar, ORANYE_EFEK, (m["rect"].centerx, m["rect"].centery - 6), UKURAN_MUSUH // 2)
        pygame.draw.circle(layar, MERAH_METEOR, (m["rect"].centerx, m["rect"].centery), UKURAN_MUSUH // 2)
    
    for peluru in peluru_list:
        pygame.draw.rect(layar, KUNING_GLOW, (peluru.x - 2, peluru.y, peluru.width + 4, peluru.height))
        pygame.draw.rect(layar, KUNING_LASER, peluru)
        
    gambar_pesawat(layar, pemain.x, pemain.y)
        
    teks_skor = font_skor.render(f"Skor: {skor}", True, PUTIH)
    layar.blit(teks_skor, (LEBAR - teks_skor.get_width() - 25, 20))

    # 7. Logika Tabrakan Player & Game Over
    hitbox_pemain = pemain.inflate(-6, -6)
    for m in musuh_list:
        if hitbox_pemain.colliderect(m["rect"]):
            # Menggambar teks Game Over ke layar sebelum masuk jeda delay
            teks_over = font_game_over.render("GAME OVER", True, MERAH_METEOR)
            teks_info = font_skor.render(f"Skor Akhir: {skor} | Restart Otomatis...", True, PUTIH)
            
            layar.blit(teks_over, (LEBAR // 2 - teks_over.get_width() // 2, TINGGI // 2 - 60))
            layar.blit(teks_info, (LEBAR // 2 - teks_info.get_width() // 2, TINGGI // 2 + 20))
            pygame.display.update()
            
            # Cara delay yang lebih aman agar OS tidak menganggap aplikasi freeze/crash
            waktu_awal = pygame.time.get_ticks()
            menunggu = True
            while menunggu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if pygame.time.get_ticks() - waktu_awal > 3000: # Jeda 3 detik
                    menunggu = False
            
            # Reset Total Game State
            pemain.x = 375
            peluru_list.clear()
            skor = 0
            for r_m in musuh_list:
                r_m["rect"].y = random.randint(-400, -50)
                r_m["rect"].x = random.randint(0, LEBAR - UKURAN_MUSUH)
            pygame.event.clear()
            break

    pygame.display.update()
    jam.tick(60)

pygame.quit()
sys.exit()

# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ===================================
# Latihan 4: Kombinasi Huruf
# ===================================

def kombinasi(n, hasil=""):
    
    if len(hasil) == n: # Berhenti ketika jumlah huruf sesuai dengan n
        print(hasil)
        return
    
    # Mengeksplorasi semua cabang yang dimulai dengan "A"
    kombinasi(n, hasil + "A")
    # Mengeksplorasi semua cabang yang dimulai dengan "B"
    kombinasi(n, hasil + "B")
    
kombinasi(2)    

# ALUR:
# 1. Mulai dari hasil="" (kosong).
# 2. Masuk ke cabang A sampai mentok n=2 (AA), lalu cetak.
# 3. Mundur satu langkah, ambil cabang B (AB), lalu cetak.
# 4. Mundur ke awal banget, ambil cabang B besar (B).
# 5. Ulangi proses: masuk ke cabang A (BA) cetak, lalu cabang B (BB) cetak.
# 6. Total kombinasi = 2^n (2^2 = 4).

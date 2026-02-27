# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ===================================
# Latihan 3: Mencari Nilai Maksimum
# ===================================

def cari_maks(data, index=0):
    # Base case: Titik henti ketika saat index mencapai ujung list, kemudian mengembalikan elemen terakhir sebagai pembanding awal
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case: Menunda pengecekan index saat ini dan lanjut ke index berikutnya. Program akan memeriksa hingga ujung list sebelum mulai membandingkan
    maks_sisa = cari_maks(data, index + 1)
    
    if data[index] > maks_sisa: # Membandingkan elemen saat ini dengan hasil terbesar dari sisa list. Nilai yang lebih besar akan return ke stack sebelumnya 
        return data[index]
    else:
        return maks_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum: ", cari_maks(angka))

# Alur:
# 1. cari_maks([3,7,2,9,5], 0) -> panggil index 1
# 2. cari_maks([3,7,2,9,5], 1) -> panggil index 2
# 3. cari_maks([3,7,2,9,5], 2) -> panggil index 3
# 4. cari_maks([3,7,2,9,5], 3) -> panggil index 4
# 5. cari_maks([3,7,2,9,5], 4) -> Base Case: return 5 (elemen terakhir)
# 6. Unwinding (Bandingkan balik):
#    - index 3 (9) vs 5 -> return 9
#    - index 2 (2) vs 9 -> return 9
#    - index 1 (7) vs 9 -> return 9
#    - index 0 (3) vs 9 -> Hasil Akhir: 9
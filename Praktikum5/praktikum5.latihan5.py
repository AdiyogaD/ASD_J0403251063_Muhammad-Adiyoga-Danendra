# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: # Base case: Titik henti ketika saat panjang hasil mencapai panjang yang diinginkan
        print("PIN:", hasil)
        return
 
    for angka in ["0", "1", "2"]: # Recursive case: Menambah angka ke hasil dan memanggil fungsi secara rekursif
        buat_pin(panjang, hasil + angka)

buat_pin(3)

''' 
Cara mencegah angka yang sama muncul berulang

Gunakan 'if angka not in hasil' sebelum rekursif,
kondisi ini akan memastikan setiap iterasi hanya memproes angka yang unik
Jika angka sudah ada di dalam 'hasil', maka rekursif tidak akan dipanggil
Sehingga angka yang sama tidak akan muncul berulang
 '''
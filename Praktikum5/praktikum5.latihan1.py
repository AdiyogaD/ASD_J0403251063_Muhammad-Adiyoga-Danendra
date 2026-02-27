# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ===================================
# Latihan 1: Rekursi Pangkat
# ===================================

def pangkat(a, n):

    # Base case: titik berhenti rekursi
    if n == 0: # Jika nilai n sudah mencapai 0, maka akan berhenti memanggil fungsinya sendiri
        return 1 # akan mengembalikan nilai menjadi 1

    # Recursive case: Fungsi akan memanggil dirinya sendiri sambil mengurangi nilai pangkatnya satu per satu
    return a * pangkat(a, n - 1) # Setiap pemanggilan akan mengurangi n sebesar 1

print(pangkat(2, 4)) # Output: 16 

# Alur:
# 1. pangkat(2, 4) -> return 2 * pangkat(2, 3)
# 2. pangkat(2, 3) -> return 2 * pangkat(2, 2)
# 3. pangkat(2, 2) -> return 2 * pangkat(2, 1)
# 4. pangkat(2, 1) -> return 2 * pangkat(2, 0)
# 5. pangkat(2, 0) -> return 1 (Base Case)
# 6. Hasil Akhir: 2 * 2 * 2 * 2 * 1 = 16
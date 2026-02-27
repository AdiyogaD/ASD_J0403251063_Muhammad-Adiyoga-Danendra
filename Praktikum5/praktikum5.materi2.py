# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ======================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ======================================

def hitung (n):
    # Base case
    if n == 0:
        print("Selesai")
        return

    print("Masuk: ", n)  # fase stacking
    hitung(n - 1)        # Pemanggilan Rekursif
    print("Keluar: ", n) # Fase unwinding

hitung(3)
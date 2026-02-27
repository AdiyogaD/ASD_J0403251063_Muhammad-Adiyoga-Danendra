# ===================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ===================================

# ===================================
# Latihan 2: Tracing Rekursi
# ===================================

def countdown(n):
    
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk: ", n) # Proses stack
    countdown(n-1) # Pemanggilan rekursif, perintah akan menunda baris di bawahnya dan disimpan kedalam stack
    print("Keluar: ", n) # Karena dengan prinsip Last In, First Out, perintah akan dieksekusi setelah pemanggilan rekursif selesai. Muncul terbalik karena perintah terakhir yang ditunda adalah (n=1)
countdown(3)
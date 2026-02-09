# ==================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : A2/P2
# ==================================

nama_file = "stok_barang.txt"

# Load Data

def baca_file(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")
            data_dict[kode] = {"nama": nama, "stok": int(stok)}
    return data_dict

# 1. Tampilkan Data

def tampilkan_data(data_dict):
    print("\n============ DAFTAR BARANG ============")
    print(f"{"Kode":<10} | {"Nama Barang":<12} | {"Total Stok":>5}")
    print("-" * 39)
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<12} | {int(stok):>5}")
        
# 2. Cari Data

def cari_data(data_dict):
    kode_cari = input("Masukkan Kode Barang yang dicari: ").strip()
    
    if kode_cari in data_dict:
        kode = data_dict[kode_cari]
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]
        
        print("===== Data Barang Ditemukan =====")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Total: {stok}")
        
    else:
        print(f"Data {kode_cari} Tidak Ditemukan. Pastikan Kode yang dimasukkan benar.")
        
# 3. Tambah Data

def tambah_data(data_dict):
    kode = input("Masukkan Kode Barang: ").strip()
    if kode in data_dict:
        print("Kode Barang sudah ada.")
        pilihan = input("Update Data? (y/n): ").strip()
        if pilihan.lower() == "y":
            update_data(data_dict)
        if pilihan.lower() == "n":
            print("Tambah Data Dibatalkan.")
        return
    
    nama = input("Masukkan Nama Barang: ").strip()
    
    try:
        stok = int(input("Masukkan Total Stok: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Tambah Data Dibatalkan")
        return
    
    if stok < 0:
        print("Total Stok tidak boleh negatif. Tambah Data Dibatalkan")
        return
    
    data_dict[kode] = {"nama": nama, "stok": stok}
    print(f"Data Barang {kode} berhasil ditambahkan")

# 4. Update barang

def update_data(data_dict):
    pilihanbrg = input("Update Barang/Hapus Barang (1/2): ").strip()
    
    if pilihanbrg == "1":
        kode = input("Masukkan Kode Barang yang ingin diubah datanya: ").strip()
        if kode not in data_dict:
            print("Kode Barang tidak ditemukan. Update dibatalkan")
            return

        nama_baru = input("Masukkan Nama Barang baru (Kosongkan jika tidak ingin mengubah): ").strip()
        if nama_baru == "":
            nama_baru = data_dict[kode]['nama']
        try:
            stok_baru = int(input("Masukkan Total Stok Baru 0-100: ").strip())
        except ValueError:
            print("Total Stok harus berupa angka. Update Dibatalkan")
            return
            
        if stok_baru < 0 or stok_baru > 100:
            print("Total Stok harus diantara 0-100. Update Dibatalkan")
            return

        stok_lama = data_dict[kode]['stok']
        data_dict[kode]['stok'] = stok_baru
        data_dict[kode]['nama'] = nama_baru
        
    elif pilihanbrg == "2":
        kode = input("Masukkan Kode Barang yang ingin dihapus: ").strip()
        if kode not in data_dict:
            print("Kode Barang tidak ditemukan. Update dibatalkan")
            return

        del data_dict[kode]
        print(f"Data Barang {kode} berhasil dihapus")
    else:
        print("Pilihan tidak valid. Update dibatalkan")
        
# 5. Simpan Ke file

def simpan_data(data_dict, nama_file):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode, info in data_dict.items():
            file.write(f"{kode},{info['nama']},{info['stok']}\n")
    print(f"Data berhasil disimpan ke {nama_file}")
    
# =========== MENU ================

def main():
    buka_data = baca_file(nama_file)
    
    while True:
        print("\n========== MENU STOK BARANG ==========")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode")
        print("3. Tambah Barang Baru")
        print("4. Update Data Barang")
        print("5. Simpan Data Ke File")
        print("0. Keluar")
        print("======================================")
        
        pilihan = input("Masukkan Pilihan (1/2/3/4/5/0): ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            tambah_data(buka_data)
        elif pilihan == "4":
            update_data(buka_data)
        elif pilihan == "5":
            simpan_data(buka_data, nama_file)
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()
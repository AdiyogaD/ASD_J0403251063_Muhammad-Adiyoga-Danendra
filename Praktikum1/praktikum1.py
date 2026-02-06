#====================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Membaca seluruh isi file data
#====================================================================

# membuka file dalam mode read ("r")
print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    isi_file = file.read() # mengambil dan menyimpan semua data dalam satu variabel
print(isi_file)

print("tipe_data 1", type(isi_file))

# membuka file per baris
print("===Membuka file per baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() # menghilangkan karakter baris baru (\n)
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)
        
        
#====================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsing Data
#====================================================================

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") # pecah data menjadi satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai) # tampilkan satuan data dalam bentuk kolom
        
#====================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3: Membaca Data dan Menyimpannya ke Struktur Data List
#====================================================================

data_list = [] # inisialisasi list untuk menampung data

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai= baris.split(",")
        data_list.append([nim,nama,int(nilai)]) # menyimpan data ke list
        
print("=== Menampilkan List====")
print(data_list)
print("contoh record ke 1", data_list[0])
print("contoh record ke 2", data_list[1])

print("Jumlah Record", len(data_list))

#====================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4: Membaca Data dan Menyimpannya ke Struktur Data Dictionary
#====================================================================

data_dict = {}

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        # simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
        
print("=== Menampilkan Data Dictionary ===")
print(data_dict)
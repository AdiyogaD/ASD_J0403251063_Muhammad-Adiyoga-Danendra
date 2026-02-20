# =============================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A2
# =============================================

# =============================================
# Implementasi Dasar : Stack
# =============================================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data # menyimpan nilai atau data pada list
        self.next = None # pointer ini menunjuk ke node berikutnya (awal=none)

# Stack ada operasi push(memasukkan head baru) dan pop(menghapus head)
# A -> B -> C -> None

class stack:
    def __init__(self):
        self.top = None # top meunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
         return self.top is None # stack kosong jika = none

    def push(self,data):
        # 1 membuat node baru
        nodeBaru = Node(data) # Instantiasi/memanggil konstruktor pada class node

        #2 node baru harus menunjuk ke top yang lama(head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): # mengambil/menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data 
        self.top = self.top.next
        return data_terhapus
    
    def peek(self):
         # melihat data yang paling atas tanpa menghapus
         if self.is_empty():
              return None
         return self.top.data

    def tampilkan(self):
            current = self.top
            print("Top", end=" -> ")
            while current is not None:
                 print(current.data, end=" -> ")
                 current = current.next
            print("None")

# Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
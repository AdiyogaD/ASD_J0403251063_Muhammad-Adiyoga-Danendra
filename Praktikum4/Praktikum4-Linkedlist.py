# =============================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A2
# =============================================

# =============================================
# Implementasi Dasar : Node pada Linked List
# =============================================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data # menyimpan nilai atau data pada list
        self.next = None # pointer ini menunjuk ke node berikutnya (awal=none)
    
# 1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Traversal : Menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya
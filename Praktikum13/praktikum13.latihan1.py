# Nama : Muhammad Adiyoga Danendra
# NIM : J0403251063
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:         # melakukan iterasi setiap edge di graph
    print(edge)             # menampilkan pasangan vertex

print("\nSpanning Tree:")    
for edge in spanning_tree:   # melakukan iterasi edge hasil spanning tree
    print(edge)             # menampilkan edge yang terpilih

print("\nJumlah edge graph =", len(edges))          # menghitung semua edge di graph
print("Jumlah edge spanning tree =", len(spanning_tree))  # n-1 vertex


# ================================ Pertanyaan ===============================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Perbedaannya adalah graph awal bisa memiliki cycle sedangkan spanning tree tidak memiliki cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Secara definisi, spanning tree tidak boleh memiliki cycle.
# Karena, jika spanning tree memiliki cycle, bukan hanya definisinya saja yang berubah,
# efisiensi dan konsumsi resource juga menjadi tidak optimal.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jumlah edge pada spanning tree selalu lebih sedikit dari graph awal karena 
# spanning tree adalah graph yang tidak memiliki cycle. (n-1 edges)
# ==========================================================================
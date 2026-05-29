# Nama : Muhammad Adiyoga Danendra
# NIM : J0403251063
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================
# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),
 (2, 'A', 'C'),
 (3, 'B', 'D'),
 (4, 'A', 'B'),
 (5, 'A', 'D')
]
# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()  # menyimpan node yang sudah masuk MST
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana

    if u not in connected or v not in connected:  # skip jika kedua node sudah terhubung (cycle)
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)  # menandai node sudah masuk MST
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# ================================ Pertanyaan ===============================
# Jawaban Analisis:

# 1. Edge mana yang dipilih pertama kali?
# Edge (C, D) dengan bobot 1 dipilih pertama kali karena merupakan edge dengan bobot terkecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Algoritma Kruskal menggunakan prinsip greedy, yaitu memilih edge dengan bobot terkecil
# untuk meminimalkan total bobot MST.

# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6. (1 + 2 + 3)

# 4. Mengapa edge tertentu tidak dipilih?
# Edge (A, B) dan (A, D) tidak dipilih karena akan membentuk cycle.


# ===========================================================================
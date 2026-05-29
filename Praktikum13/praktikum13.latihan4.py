# Nama : Muhammad Adiyoga Danendra
# NIM : J0403251063
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Weighted graph: representasi jaringan antar gedung
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):
    visited = set([start]) # menandai node awal sudah dikunjungi
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor)) # memasukkan semua edge dari node awal

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges) # mengambil edge dengan bobot terkecil

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'GedungA')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total biaya =", total)

# ================================ Pertanyaan ===============================

# Jawaban Analisis:

# 1. Algoritma apa yang digunakan?
# Algoritma Prim

# 2. Edge mana saja yang dipilih?
# ('GedungA', 'GedungC', 2)
# ('GedungC', 'GedungD', 1)
# ('GedungD', 'GedungB', 3)

# 3. Berapa total biaya minimum?
# 6

# 4. Mengapa MST cocok digunakan pada kasus ini?
# MST cocok digunakan pada kasus ini karena pada kasus ini ingin meminimalkan total biaya 
# pemasangan kabel untuk menghubungkan semua gedung.

# ===========================================================================
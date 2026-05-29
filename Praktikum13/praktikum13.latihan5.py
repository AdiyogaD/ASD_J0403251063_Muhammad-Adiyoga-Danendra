# Nama : Muhammad Adiyoga Danendra
# NIM : J0403251063
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Graf berbobot: representasi jaringan jalan antar kota
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},
    'Depok':   {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
}

# Algoritma Prim: mulai dari satu node, expand ke tetangga terdekat
def prim(graph, start):
    visited = set([start])
    edges = []

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)  # Ambil edge terkecil

        if v not in visited:  # Skip jika sudah terhubung (mencegah cycle)
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Expand ke tetangga baru dari node yang baru masuk
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'Bogor')

# Output MST dan total bobot minimum
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ================================ Pertanyaan ===============================
# Jawaban Analisis:

# 1. Kasus apa yang dipilih?
# Kasus 1 . Jaringan Jalan Antar Kota


# 2. Algoritma apa yang digunakan?
# Algoritma Prim

# 3. Edge mana saja yang dipilih dalam MST?
# ('Bogor', 'Depok', 2)
# ('Depok', 'Jakarta', 3)
# ('Depok', 'Bandung', 4)

# 4. Berapa total bobot MST?
# Total bobot MST = 9

# 5. Mengapa edge tertentu tidak dipilih?
# Edge (Bogor-Jakarta) dan (Jakarta-Bandung) tidak dipilih karena
# node-node tersebut sudah terhubung lewat Depok. Jika dipilih, akan membentuk cycle.
# ===========================================================================
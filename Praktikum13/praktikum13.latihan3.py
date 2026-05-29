# Nama : Muhammad Adiyoga Danendra
# NIM : J0403251063
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])  # menandai node awal sudah dikunjungi

    edges = [] 

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))  # masukkan semua edge dari node awal
    
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)  # mengambil edge dengan bobot terkecil

        if v not in visited: 
            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))  # menambah edge baru dari node yang baru masuk
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)
    
print("Total bobot =", total)

# ================================ Pertanyaan ===============================

# Jawaban Analisis:

# 1. Node awal apa yang digunakan?
# Node A

# 2. Edge mana yang dipilih pertama kali?
# Edge (A, C) dengan bobot 2

# 3. Bagaimana Prim menentukan edge berikutnya?
# Algoritma Prim akan menentukan edge berikutnya dengan memilih
# edge dengan bobot terkecil dari node yang sudah dikunjungi

# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Kruskal: Mengurutkan semua edge berdasarkan bobot terkecil, lalu memilih edge 
#          yang tidak membentuk cycle
# Prim: Memilih edge dengan bobot terkecil dari node yang sudah dikunjungi

# ===========================================================================
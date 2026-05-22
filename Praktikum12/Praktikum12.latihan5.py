# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Jarak Kota
# Algoritma: Dijkstra
# ==========================================================
import heapq

# Graph lokasi kota
# Menyesuaikan agar hasil jarak dari Bogor ke Bandung = 8
graph = {
 'Bogor': {'Jakarta': 4, 'Depok': 2},
 'Depok': {'Bandung': 6},  # Bogor -> Depok (2) + Depok -> Bandung (6) = 8
 'Jakarta': {},
 'Bandung': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
    
hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for lokasi, jarak in hasil.items():
    print(f"Bogor -> {lokasi} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Node yang memiliki jarak paling kecil dari node awal adalah Depok dengan jarak 2

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Node yang memiliki jarak paling besar dari node awal adalah Bandung dengan jarak 8

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja pada kasus yang saya buat dengan cara mencari jarak terpendek dari node awal ke seluruh node lain

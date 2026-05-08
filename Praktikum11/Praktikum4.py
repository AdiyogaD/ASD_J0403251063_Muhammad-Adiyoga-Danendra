# ============================================
# Nama         : Muhammad Adiyoga Danendra
# NIM          : J0403251063
# Kelas        : TPL A/P2
# Studi Kasus  : Jaringan Komputer
# ============================================

# =================================
# Nodes dan edges jaringan komputer
# =================================

# Nodes:
# PC1 → Switch1
# Switch1 → PC2
# Switch1 → PC3
# Switch1 → Server
# Server → PC4
# PC1 → PC4

nodes = ["PC1", "PC2", "PC3", "PC4", "Switch1", "Server"]
edges = [("PC1", "Switch1"),("Switch1", "PC2"),("Switch1", "PC3"),("Switch1", "Server"),("Server", "PC4"),("PC1", "PC4")
]

# ==================================
# Adjacency List (Undirected)
# ==================================

# buat dictionary kosong, tiap node jadi key
adj_list = {node: [] for node in nodes}

for u, v in edges:
    adj_list[u].append(v) # u terhubung ke v
    adj_list[v].append(u) # v juga terhubung balik ke u

# =================================
# Adjacency Matriks
# =================================

n = len(nodes) # jumlah node = ukuran matriks
node_index = {node: i for i, node in enumerate(nodes)} # mapping nama node ke angka index

adj_matrix = [[0] * n for _ in range(n)] # bikin matriks n x n isi 0

for u, v in edges: 
    i, j = node_index[u], node_index[v] # ambil index angka dari nama node
    adj_matrix[i][j] = 1 # u terhubung ke v
    adj_matrix[j][i] = 1 # v juga terhubung balik ke u

# ================================
# Menampilkan Adjency List
# ================================

print("Adjacency List:\n")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

# ================================
# Menampilkan Adjency Matriks
# ================================

print("\nAdjacency Matrix:\n")
for row in adj_matrix:
    print(row)
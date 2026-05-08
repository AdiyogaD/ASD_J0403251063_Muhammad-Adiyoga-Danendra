# ============================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ============================================

def createGraph(V, edges):
    # bikin matrix V x V, isi awal semua 0
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        # karena undirected, dua arah harus diisi
        mat[u][v] = 1
        mat[v][u] = 1
        
    return mat

if __name__ == "__main__":
    V = 4

    # setiap sublist = satu edge [u, v]
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    mat = createGraph(V, edges)
    
    # menampilkan adjacency matrix
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print([ mat[i][j] ], end=" ")
        print()

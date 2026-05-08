# ============================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ============================================

def convertToList(V, matrix):
    # siapkan adjacency list kosong sebanyak jumlah node
    adj = [[] for _ in range(V)]
    
    # cek tiap cell di matrix
    for i in range(V):
        for j in range(V):
            # kalau nilainya 1 berarti ada edge dari i ke j
            if matrix[i][j] == 1:
                adj[i].append(j)  # tambahin j sebagai tetangga i
    
    return adj

if __name__ == "__main__":
    V = 4
    # matrix[i][j] = 1 artinya node i terhubung ke node j
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    adj = convertToList(V, matrix)
    
    # menampilkan adjacency list
    print("Adjacency List Representation:")
    for i in range(V):
        print(f"{i}:", end=" ")
        for j in adj[i]:
            print(j, end=" ")
        print()

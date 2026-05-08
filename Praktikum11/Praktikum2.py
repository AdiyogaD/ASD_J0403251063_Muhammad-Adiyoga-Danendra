# ============================================
# Nama  : Muhammad Adiyoga Danendra
# NIM   : J0403251063
# Kelas : TPL A/P2
# ============================================

def createGraph(nodes, edges):
    # buat dictionary, tiap node jadi key dengan value list kosong
    adj = {node: [] for node in nodes}
    
    for it in edges:
        u = it[0]
        v = it[1]
        # undirected jadi kedua arah ditambahin
        adj[u].append(v)
        adj[v].append(u)
        
    return adj

if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D']
    # format edge [node asal, node tujuan]
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]
    adj = createGraph(nodes, edges)
    
    # menampilkan adjacency list
    print("Adjacency List Representation:")
    for node in adj:
        print(f"{node}:", end=" ")
        for neighbor in adj[node]:
            print(neighbor, end=" ")
        print()

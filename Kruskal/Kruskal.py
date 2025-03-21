def Kruskal(v: int, edges: list[int]):
    '''
    v       : the number of vertices
    edges   : [start, end, weight]
    '''

    # union-find (disjoint set)
    uf = list(range(v + 1))

    # find operation
    def find(n):
        if uf[n] == n:
            return n
            
        root_node = find(uf[n])
        
        uf[n] = root_node
        
        return root_node
    
    # union operation
    def union(a, b):
        A = find(a)
        B = find(b)
        
        uf[A] = B

    # sort edges by their weight
    edges.sort(key = lambda x:x[2])

    mst = 0

    for e in edges:
        A, B, w = e[0], e[1], e[2]
        
        if find(A) != find(B):
            union(A, B)
            mst += w

    return mst

class UnionFind:
    def __init__(self, n: int):
        self.uf: list[int] = list(range(n + 1))
        self.size: list[int] = [1] * (n + 1)
        
    def find(self, x: int):
        if x == self.uf[x]:
            return x
        
        root_node = self.find(self.uf[x])
        self.uf[x] = root_node
        
        return root_node
        
    def union(self, x: int, y: int):
        X = self.find(x)
        Y = self.find(y)
        
        self.uf[Y] = X
        
        # update size info
        self.size[X] += self.size[Y]
        
    def get_size(self, x: int):
        return self.size[self.find(x)]
        
'''
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

print(uf.get_size(1))  # 3 (1, 2, 3이 같은 집합)
print(uf.get_size(4))  # 2 (4, 5가 같은 집합)
print(uf.get_size(6))  # 1 (6은 혼자 있음)
print(uf.uf)
'''
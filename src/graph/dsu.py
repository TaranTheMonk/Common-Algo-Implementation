class DSU:
    def __init__(self, N: int):
        # every node's init parent is itself
        self.parent = list(range(N))

        # size of each component
        self.rank = [0] * N

    def find(self, x: int) -> int:
        # if x is not the root
        if self.parent[x] != x:
            parent = self.find(self.parent[x])
            # compress the path
            self.parent[x] = parent
            return self.parent[x]
        else:
            return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        else:
            # merge to the parent with larger rank
            if self.rank[xr] >= self.rank[yr]:
                self.parent[yr] = xr
                self.rank[xr] += self.rank[yr]
                self.rank[yr] = 0
            else:
                self.parent[xr] = yr
                self.rank[yr] += self.rank[xr]
                self.rank[xr] = 0

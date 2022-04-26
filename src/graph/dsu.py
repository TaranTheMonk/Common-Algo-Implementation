class DSU:
    """
    data structure to find and merge components in logrithm time complexity
    """

    def __init__(self, n: int):
        """
        1. only when dsu.parent[n] == n, n is the root!
        2. set(dsu.parent) doesn't represent to all unique components:
            dsu.parent -> [0, 0, 1]
            dsu.parent[2] -> 1
            dsu.parent[1] -> 0
            dsu.parent[0] -> 0

            set(dsu.parent) has 2 elements, but there's only one component!
        :param n:
        """

        # every node's init parent is itself
        self.parent = list(range(n))

        # size of each component
        self.rank = [1] * n

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

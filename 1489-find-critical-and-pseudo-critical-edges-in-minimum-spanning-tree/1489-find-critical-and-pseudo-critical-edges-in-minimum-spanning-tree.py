class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                A = self.find(x)
                B = self.find(y)

                if A == B:
                    return False

                if self.size[A] < self.size[B]:
                    A, B = B, A

                self.parent[B] = A
                self.size[A] += self.size[B]

                return True

        # Save original indices
        edges = [edge + [i] for i, edge in enumerate(edges)]

        # Kruskal needs sorted edges
        edges.sort(key=lambda x: x[2])

        def mst(skip=-1, force=-1):

            d = DSU(n)
            cost = 0
            count = 0

            # Force one edge first
            if force != -1:
                u, v, w, idx = edges[force]

                if d.union(u, v):
                    cost += w
                    count += 1

            for i in range(len(edges)):

                if i == skip or i == force:
                    continue

                u, v, w, idx = edges[i]

                if d.union(u, v):
                    cost += w
                    count += 1

                    if count == n - 1:
                        return cost

            return float("inf")

        normal = mst()

        critical = []
        pseudo = []

        for i in range(len(edges)):

            # Remove edge
            if mst(skip=i) > normal:
                critical.append(edges[i][3])

            # Force edge
            elif mst(force=i) == normal:
                pseudo.append(edges[i][3])

        return [critical, pseudo]
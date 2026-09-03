class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # Not enough cables to ever connect n computers
        if len(connections) < n - 1:
            return -1

        class DSU:
            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.size = [1] * n

            def find(self, x):
                if self.parents[x] != x:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self, x, y):
                A = self.find(x)
                B = self.find(y)

                if A == B:
                    return False

                if self.size[A] < self.size[B]:
                    A, B = B, A

                self.parents[B] = A
                self.size[A] += self.size[B]

                return True

        d = DSU(n)

        components = n

        for u, v in connections:
            if d.union(u, v):
                components -= 1

        return components - 1
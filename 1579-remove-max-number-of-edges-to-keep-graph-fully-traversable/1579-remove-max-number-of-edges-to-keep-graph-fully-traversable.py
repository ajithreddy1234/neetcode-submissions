class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class DSU:
            def __init__(self, n):
                self.parent = [i for i in range(n + 1)]
                self.size = [1] * (n + 1)
                self.com = n

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return False

                if self.size[px] < self.size[py]:
                    px, py = py, px

                self.parent[py] = px
                self.size[px] += self.size[py]
                self.com -= 1

                return True

        alice = DSU(n)
        bob = DSU(n)

        removed = 0

        # 1. Type 3 first
        for t, u, v in edges:
            if t == 3:
                usedAlice = alice.union(u, v)
                usedBob = bob.union(u, v)

                # removable only if BOTH don't need it
                if not usedAlice and not usedBob:
                    removed += 1

        # 2. Alice edges
        for t, u, v in edges:
            if t == 1:
                if not alice.union(u, v):
                    removed += 1

        # 3. Bob edges
        for t, u, v in edges:
            if t == 2:
                if not bob.union(u, v):
                    removed += 1

        if alice.com != 1 or bob.com != 1:
            return -1

        return removed
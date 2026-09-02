class Solution:
    def findTheCity(
        self,
        V: int,
        edges: List[List[int]],
        distanceThreshold: int
    ) -> int:

        dist = [
            [float("inf")] * V
            for _ in range(V)
        ]

        for i in range(V):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)

        # First finish Floyd-Warshall
        for k in range(V):
            for u in range(V):
                for v in range(V):
                    dist[u][v] = min(
                        dist[u][v],
                        dist[u][k] + dist[k][v]
                    )

        # NOW all distances are final
        min_count = float("inf")
        min_val = -1

        for u in range(V):

            count = 0

            for v in range(V):
                if u != v and dist[u][v] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                min_val = u

        return min_val
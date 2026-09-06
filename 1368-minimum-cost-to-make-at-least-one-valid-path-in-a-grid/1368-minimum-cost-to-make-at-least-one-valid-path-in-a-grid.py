class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        adj = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        rows = len(grid)
        cols = len(grid[0])

        visited = [
            [float("inf") for _ in range(cols)]
            for _ in range(rows)
        ]

        visited[0][0] = 0

        heap = [(0, 0, 0)]

        while heap:

            cost, x, y = heapq.heappop(heap)

            if visited[x][y] < cost:
                continue

            if x == rows - 1 and y == cols - 1:
                return cost

            v = grid[x][y]

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:

                    if (dx, dy) == adj[v]:
                        weight = 0
                    else:
                        weight = 1

                    new_cost = cost + weight

                    if new_cost < visited[nx][ny]:

                        visited[nx][ny] = new_cost

                        heapq.heappush(
                            heap,
                            (new_cost, nx, ny)
                        )

        return 0

        
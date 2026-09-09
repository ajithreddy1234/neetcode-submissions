class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dp[row][col1][col2]
        # = maximum cherries collectable from this state to the bottom
        dp = [
            [[float("-inf")] * cols for _ in range(cols)]
            for _ in range(rows)
        ]

        # Base case: last row
        for col1 in range(cols):
            for col2 in range(cols):
                if col1 == col2:
                    dp[rows - 1][col1][col2] = grid[rows - 1][col1]
                else:
                    dp[rows - 1][col1][col2] = (
                        grid[rows - 1][col1]
                        + grid[rows - 1][col2]
                    )

        # Fill from bottom to top
        for row in range(rows - 2, -1, -1):
            for col1 in range(cols):
                for col2 in range(cols):

                    # cherries collected on current row
                    if col1 == col2:
                        current = grid[row][col1]
                    else:
                        current = grid[row][col1] + grid[row][col2]

                    best = float("-inf")

                    # 3 moves for robot 1 × 3 moves for robot 2
                    for move1 in [-1, 0, 1]:
                        for move2 in [-1, 0, 1]:

                            next_col1 = col1 + move1
                            next_col2 = col2 + move2

                            if (
                                0 <= next_col1 < cols
                                and 0 <= next_col2 < cols
                            ):
                                best = max(
                                    best,
                                    dp[row + 1][next_col1][next_col2]
                                )

                    dp[row][col1][col2] = current + best

        # Initial robot positions
        return dp[0][0][cols - 1]
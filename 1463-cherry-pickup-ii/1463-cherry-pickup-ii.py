class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[[float("-inf") for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        print(dp)
        for col1 in range(cols):
            for col2 in range(cols):
                if col1==col2:
                    dp[rows-1][col1][col2]=grid[rows-1][col1]
                else:
                    dp[rows-1][col1][col2]=grid[rows-1][col1]+grid[rows-1][col2]
        for r in range(rows-2,-1,-1):
            for col1 in range(cols):
                for col2 in range(cols):
                    if col1==col2:
                        dp[r][col1][col2]=grid[r][col1]
                    else:
                        dp[r][col1][col2]=grid[r][col1]+grid[r][col2]
                    best=float("-inf")
                    for m1 in [-1,0,1]:
                        for m2 in [-1,0,1]:
                            nx=col1+m1
                            ny=col2+m2
                            if 0<=nx<cols and 0<=ny<cols:
                                best=max(best,dp[r+1][nx][ny])
                    dp[r][col1][col2]+=best
        return dp[0][0][cols-1]

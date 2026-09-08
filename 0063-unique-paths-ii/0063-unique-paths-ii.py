class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        obstacleGrid[0][0]=1
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1 and ((i,j)!=(0,0)):
                    obstacleGrid[i][j]=0
                    continue
                if i>0:
                    obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                if j>0:
                    obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        print(obstacleGrid)
        return obstacleGrid[rows-1][cols-1]

        
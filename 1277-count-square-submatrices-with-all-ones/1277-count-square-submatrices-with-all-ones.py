class Solution:
    def countSquares(self, matrix: List[List[str]]) -> int:
        print(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        ma = 0
        x=defaultdict(int)
        dp=[[0 for i in range(cols)] for i in range(rows)]
        print(dp)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    print(x,i,j)
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    mg=dp[i][j]
                    if mg==1:
                        x[mg]+=1
                    else:
                        while mg>0:
                            x[mg]+=1
                            mg-=1
        return sum(list(x.values()))
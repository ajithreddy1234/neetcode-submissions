from collections import deque
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ma = 0
        dp=[[0 for i in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    ma=max(ma,dp[i][j])
        print(dp)
        return ma*ma
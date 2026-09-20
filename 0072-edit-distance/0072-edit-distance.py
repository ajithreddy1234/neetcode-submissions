class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        dp=[[-1 for i in range(n2+1)] for i in range(n1+1)]
        def solve(i,j):
            if j==n2:
                return n1-i
            if i==n1:
                return n2-j
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                ans=solve(i+1,j+1)
            else:
                ans1=1+solve(i+1,j+1)
                ans2=1+solve(i,j+1)
                ans3=1+solve(i+1,j)
                print(ans1,ans2,ans3)
                ans=min(ans1,ans2,ans3)
            dp[i][j]=ans
            return ans
        return solve(0,0)



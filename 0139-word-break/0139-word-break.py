class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        memo=[[-1 for i in range(n+1)] for i in range(n+1)]
        seen=set(wordDict)
        def solve(i,j):
            if j==n:
                return s[i:j] in seen
            if memo[i][j]!=-1:
                return memo[i][j]
            word=s[i:j+1]
            if word in seen:
                b=solve(j+1,j+1)
                a=solve(i,j+1)
                best=a or b
            else:
                best=solve(i,j+1)
            memo[i][j]=best
            return best
        m=solve(0,0)
        return m
        
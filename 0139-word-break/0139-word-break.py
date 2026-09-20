class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n=len(s)
        memo=[-1 for i in range(n+1)]
        seen=set(wordDict)
        def solve(i):
            if i==n:
                return True
            if memo[i]!=-1:
                return memo[i]
            for j in range(i+1,n+1):
                word=s[i:j]
                if word in seen:
                    if solve(j):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        return solve(0)
        
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        s=[]
        def dfs(st,o,c):
            nonlocal s
            if o==n and c==n:
                s.append(st)
            if o<n:
                dfs(st+"(",o+1,c)
            if o>c:
                dfs(st+")",o,c+1)
        dfs("",0,0)
        return s
        
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res=0
        visited=set()
        n=len(isConnected)
        def dfs(city):
            if city in visited:
                return
            visited.add(city)
            for  i in range(n):
                if i not in visited and isConnected[city][i]==1:
                    dfs(i)
        for city in range(n):
            if city not in visited:
                res+=1
                dfs(city)
        return res

        
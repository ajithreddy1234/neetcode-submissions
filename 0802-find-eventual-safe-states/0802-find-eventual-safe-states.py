class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        hot=[0]*n
        def dfs(node):
            if hot[node]==1:
                return False
            if hot[node]==2:
                return True
            if hot[node]==3:
                return False
            hot[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    hot[nei]=3
                    hot[node]=3
                    return False
            hot[node]=2
            return True
        final=[]
        for i in range(n):
            if dfs(i):
                final.append(i)
        return final


                
        
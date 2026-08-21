class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        x=defaultdict(list)
        for l,r in edges:
            x[l].append(r)
            x[r].append(l)
        vis=set()
        def dfs(node):
            if node in vis:
                return False
            if node==destination:
                return True
            vis.add(node)
            for ne in x[node]:
                if dfs(ne):
                    return True
            return False
        return dfs(source)
            
        
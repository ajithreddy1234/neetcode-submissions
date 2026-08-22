class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for s,e in edges:
            adj[e].append(s)
            adj[s].append(e)
        visited=set()
        def dfs(i):
            nonlocal count
            if i in visited:
                return
            count+=1
            visited.add(i)
            for m in adj[i]:
                dfs(m)
        fin=[]
        for i in range(n):
            if i in adj:
                if i not in visited:
                    count=0
                    dfs(i)
                    fin.append(count)
            else:
                fin.append(1)
        ans=0
        if len(fin)<=1:
            return 0
        se=0
        ans=0
        for k in fin:
            ans+=se*k
            se+=k
        return ans
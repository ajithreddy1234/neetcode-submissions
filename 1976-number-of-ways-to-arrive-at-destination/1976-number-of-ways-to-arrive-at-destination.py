class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=7+10**9
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        final=[]
        first=True
        heap=[(0,0)]
        dist=[float("inf")]*n
        dp=[0]*n
        dist[0]=0
        dp[0]=1
        while heap:
            weight,node=heapq.heappop(heap)
            if dist[node]<weight:
                continue
            for nei,w in adj[node]:
                if weight+w<dist[nei]: 
                    dist[nei]=weight+w
                    heapq.heappush(heap,(weight+w,nei))
                    dp[nei]=dp[node]
                elif weight+w==dist[nei]:
                    dp[nei]+=dp[node]
        return dp[n-1]%mod
                
            
        
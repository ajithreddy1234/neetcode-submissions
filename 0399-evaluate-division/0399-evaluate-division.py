class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1],values[i]])
            adj[equations[i][1]].append([equations[i][0],1/values[i]])
        def find(start,end):
            if (start not in adj) or (end not in adj):
                return -1
            heap=[(1,start)]
            visited=set()
            while heap:
                wei,p=heapq.heappop(heap)
                if p==end:
                    return wei
                for nei,w in adj[p]:
                    if nei not in visited:
                        visited.add(nei)
                        heapq.heappush(heap,(wei*w,nei))
            return -1
        final=[]
        for x,y in queries:
            final.append(find(x,y))
        return final

        
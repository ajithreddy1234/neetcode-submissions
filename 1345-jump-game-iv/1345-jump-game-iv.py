class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        end=n-1
        start=0
        if start==end:
            return 0
        if arr[start]==arr[end]:
            return 1
        dq=deque([start])
        visited={start}
        adj=defaultdict(list)
        for i in range(n):
            adj[arr[i]].append(i)
        level=0
        while dq:
            for i in range(len(dq)):
                x=dq.popleft()
                if x==end:
                    return level
                li=[x+1,x-1]+adj[arr[x]]
                adj[arr[x]].clear()
                for ind in li:
                    if ind>=0 and ind<=n-1 and ind not in visited:
                        visited.add(ind)
                        dq.append(ind)
            level+=1
        return 
                


        
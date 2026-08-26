class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        state=[0]*n
        adj=defaultdict(list)
        for m,l in dislikes:
            adj[m-1].append(l-1)
            adj[l-1].append(m-1)
        for i in range(n):
            print(i)
            if state[i]!=0:
                continue
            state[i]=1
            dq=deque([i])
            while dq:
                x=dq.popleft()
                for nei in adj[x]:
                    if state[nei]==0:
                        state[nei]=-state[x]
                        dq.append(nei)
                    elif state[x]==state[nei]:
                        return False
        return True            
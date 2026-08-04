class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x=Counter(tasks)
        o=list(x.values())
        o.sort()
        m=deque(o)
        k=m.pop()
        idle=(k-1)*n
        for n in m:
            idle-=n
            if n==k:
                idle+=1
        return len(tasks)+(idle if idle>=0 else 0)
            

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen=set(deadends)
        dq=deque(["0000"])
        level=0
        visited=set()
        visited.add("0000")
        num=0
        while dq:
            for _ in range(len(dq)):
                x=dq.popleft()
                if x in seen:
                    continue
                if x==target:
                    return num
                for i in range(4):
                    for ch in [1,-1]:
                        mg=list(x)
                        mg[i]=str((int(mg[i])+ch)%10)
                        mg="".join(mg)
                        if mg not in seen and mg not in visited:
                            print(mg,num)
                            visited.add(mg)
                            dq.append(mg)
                            if mg==target:
                                return num+1
            num+=1
        return -1
            
        
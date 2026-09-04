class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank)
        dq=deque([startGene])
        level=0
        if startGene in bank:
            bank.remove(startGene)
        while dq:
            for _ in range(len(dq)):
                x=dq.popleft()
                if x==endGene:
                    return level
                for i in range(len(x)):
                    for ch in "ACGT":
                        if ch==x[i]:
                            continue
                        y=x[:i]+ch+x[i+1:]
                        if y in bank:
                            bank.remove(y)
                            dq.append(y)
            level+=1
        return -1
        
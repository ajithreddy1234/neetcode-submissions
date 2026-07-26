class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        x=Counter(s)
        see=set()
        l=0
        final=[]
        for r in range(len(s)):
            see.add(s[r])
            x[s[r]]-=1
            if x[s[r]]==0:
                see.remove(s[r])
            if len(see)==0:
                final.append(r-l+1)
                l=r+1
        return final




        
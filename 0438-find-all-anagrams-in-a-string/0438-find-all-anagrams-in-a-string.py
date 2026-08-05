class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        seen=Counter(p)
        l=0
        x=defaultdict(int)
        fin=[]
        first=True
        for r in range(len(s)):
            x[s[r]]+=1
            if r-l+1>len(p):
                x[s[l]]-=1
                if x[s[l]]==0:
                    del x[s[l]]
                l+=1
            if r-l+1==len(p) and x==seen:
                fin.append(l)

        return fin
        


        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        def check(c_s,c_t):
            if len(c_s)!=len(c_t):
                return False
            for key,value in c_s.items():
                if c_s[key]<c_t[key]:
                    return False
            return True
        if n<m:
            return ""
        c_t=Counter(t)
        c_s=defaultdict(int)
        l=0
        e_l,e_r=-float("inf"),float("inf")
        for r in range(n):
            if s[r] in c_t:
                c_s[s[r]]+=1
                while check(c_s,c_t):
                    if e_r-e_l>r-l:
                        e_l,e_r=l,r
                    if s[l] in c_s:
                        c_s[s[l]]-=1
                    if c_s[s[l]]==0:
                        del c_s[s[l]]
                    l+=1

        if e_r==float("inf") or e_l==-float("inf"):
            return ""
        return s[e_l:e_r+1]
            

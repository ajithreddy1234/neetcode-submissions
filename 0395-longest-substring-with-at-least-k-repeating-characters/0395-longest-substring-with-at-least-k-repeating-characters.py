class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        for target in range(1,27):
            print(target)
            freq=defaultdict(int)
            l=0
            unique=0
            valid=0
            for r in range(n):
                if freq[s[r]]==0:
                    unique+=1
                freq[s[r]]+=1
                if freq[s[r]]==k:
                    valid+=1
                while unique>target:
                    if freq[s[l]]==k:
                        valid-=1
                    freq[s[l]]-=1
                    if freq[s[l]]==0:
                        unique-=1
                    l+=1
                if unique==valid and unique==target:
                    print(l,r)
                    res=max(res,r-l+1)
        return res


        
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        co={"a":-k,"b":-k,"c":-k}
        for ele in s:
            co[ele]+=1
        for key,value in co.items():
            if value<0:
                return -1
        freq=defaultdict(int)
        l=0
        mi=-1
        for r in range(len(s)):
            freq[s[r]]+=1
            while freq[s[r]]>co[s[r]]:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
                
            for key,value in freq.items():
                if co[key]<freq[key]:
                    continue
                mi=max(mi,r-l+1)
        if mi==-1:
            return mi
        return len(s)-mi
                
        
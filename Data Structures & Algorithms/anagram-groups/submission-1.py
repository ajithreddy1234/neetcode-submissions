class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=strs.copy()
        final=[]
        seen=set()
        for i in range(len(m)):
            m[i]=Counter(m[i])
        for i in range(len(m)):
            if i not in seen:
                k=[strs[i]]
                seen.add(i)
                for j in range(i+1,len(m)):
                    if j not in seen and m[i]==m[j]:
                        k.append(strs[j])
                        seen.add(j)
                final.append(k)
        print(final)
        return final
            


        
        
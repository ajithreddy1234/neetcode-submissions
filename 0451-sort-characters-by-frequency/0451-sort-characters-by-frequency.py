class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s)
        mg=[]
        for key,value in x.items():
            mg.append([value,key])
        mg.sort(reverse=True)
        st=""
        for l,r in mg:
            st+=r*l
        return st
        
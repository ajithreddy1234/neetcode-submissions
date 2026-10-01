class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        val=0
        m=[]
        st=""
        for e in s:
            st+=e
            if e=="(":
                val+=1
            elif e==")":
                val-=1
            if val==0:
                m.append(st)
                st=""
        for i in range(len(m)):
            m[i]=m[i][1:-1]
        return "".join(m)
        
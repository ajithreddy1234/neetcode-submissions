class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        st=[]
        for i in range(1,n+1):
            st.append(str(i))
        def nextt(s):
            yes=False
            for i in range(len(s)-1,-1,-1):
                for j in range(len(s)-1,i,-1):
                    if s[i]<s[j]:
                        yes=True
                        s[i],s[j]=s[j],s[i]
                        sort=[]
                        for k in range(i+1,len(s)):
                            sort.append(s[k])
                        sort.sort()
                        lg=0
                        for k in range(i+1,len(s)):
                            s[k]=sort[lg]
                            lg+=1
                        break
                if yes:
                    break
            return s
        for i in range(k-1):
            nextt(st)
        return "".join(st)


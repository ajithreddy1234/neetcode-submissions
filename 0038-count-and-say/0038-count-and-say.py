class Solution:
    def countAndSay(self, n: int) -> str:
        def RL(s):
            i=0
            st=""
            c=1
            while i<len(s):
                while i<len(s)-1 and s[i]==s[i+1]:
                    i+=1
                    c+=1
                st+=(str(c)+s[i])
                i+=1
                c=1
            return st
        def CS(k):
            if k==1:
                return "1"
            return RL(CS(k-1))
        return CS(n)
        
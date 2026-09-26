class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        adj={}
        for key,value in knowledge:
            adj[key]=value
        n=len(s)
        i=0
        st=""
        while i<n:
            if i+1>0 and s[i]=="(":
                na=""
                i+=1
                while i<n and s[i]!=")":
                    na+=s[i]
                    i+=1
                if na in adj:
                    ret=adj[na]
                else:
                    ret="?"
                st+=ret
            else:
                st+=s[i]
            i+=1
        return st
        
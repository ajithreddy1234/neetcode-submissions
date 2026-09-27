class Solution:
    def reverseParentheses(self, s: str) -> str:
        mg=list(s)
        n=len(s)
        for i in range(n-1,-1,-1):
            if mg[i]=="(":
                st=[]
                j=i+1
                while mg[j]!=")":
                    st.append(mg[j])
                    j+=1
                mg=mg[:i]+st[::-1]+mg[j+1:]
                print(st)
        return "".join(mg)
            



        
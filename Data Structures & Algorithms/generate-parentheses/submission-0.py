class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def valid(s: str):
            open=0
            for c in s:
                open +=1 if c=="(" else -1
                if open<0:
                    return False
            return not open
        def ss(s:str):
            if n*2==len(s):
                if valid(s):
                    res.append(s)
                return 
            ss(s+"(")
            ss(s+")")
        ss("")
        return res


        

        


        
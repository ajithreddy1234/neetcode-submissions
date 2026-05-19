class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def backtrack(ope,clos):
            if ope==clos==n:
                res.append("".join(stack))
            if ope<n:
                stack.append("(")
                backtrack(ope+1,clos)
                stack.pop()
            if clos<ope:
                stack.append(")")
                backtrack(ope,clos+1)
                stack.pop()
        backtrack(0,0)
        return res

        

        


        
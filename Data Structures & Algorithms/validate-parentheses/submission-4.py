class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack1=[]
        stack2=[]
        ab={"(":")","[":"]","{":"}"}
        for i in s:
            if i in ab:
                stack1.append(ab[i])
            elif not stack1 or i!=stack1.pop():
                return False    
                
        return not stack1

 
        

        
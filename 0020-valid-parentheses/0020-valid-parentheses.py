class Solution:
    def isValid(self, s: str) -> bool:
        see={"(":")","[":"]","{":"}"}
        stack=[]
        for e in s:
            if e in see:
                stack.append(see[e])
            elif stack and e==stack[-1]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
            
        
class Solution:
    def isValid(self, s: str) -> bool:
        st={'(':')','[':']','{':'}'}
        stack=[]
        for ele in s:
            if stack and st[stack[-1]]==ele:
                stack.pop()
            elif ele in ")]}":
                return False
            else:
                stack.append(ele)
        return len(stack)==0
        
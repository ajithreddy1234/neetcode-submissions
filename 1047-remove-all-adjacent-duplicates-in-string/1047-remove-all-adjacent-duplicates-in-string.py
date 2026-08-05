class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for r in range(len(s)):
            if stack and stack[-1]==s[r]:
                while stack and stack[-1]==s[r]:
                    stack.pop()
            else:
                stack.append(s[r])
        return "".join(stack)
        
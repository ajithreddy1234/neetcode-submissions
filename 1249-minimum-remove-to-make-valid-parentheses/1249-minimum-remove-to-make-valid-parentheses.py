class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        x={"(":")"}
        stack=[]
        remove=set()
        for i in range(len(s)):
            if s[i] in x:
                stack.append(i)
            elif stack and x[s[stack[-1]]]==s[i]:
                stack.pop()
            elif s[i]==")":
                remove.add(i)
            else:
                continue
        remove.update(stack)
        st=""
        for i in range(len(s)):
            if i in remove:
                continue
            st+=s[i]
        return st
        



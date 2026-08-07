class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove=set()
        opens=[]
        final=""
        for i in range(len(s)):
            if s[i]=="(":
                opens.append(i)
            elif s[i]==")":
                if opens:
                    opens.pop()
                else:
                    remove.add(i)
        remove.update(opens)
        for i in range(len(s)):
            if i not in remove:
                final+=s[i]
        return final

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        l=''
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return l
            else:
                l+=strs[0][i]
        return l
        
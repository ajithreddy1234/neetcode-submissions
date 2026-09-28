class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        checker=strs[0]
        for i in range(1,len(strs)):
            j=0
            mg=min(len(checker),len(strs[i]))
            for j in range(min(len(checker),len(strs[i]))+1):
                if j<min(len(checker),len(strs[i])) and strs[i][j]!=checker[j]:
                    break
            checker=strs[i][:j]
        return checker

        
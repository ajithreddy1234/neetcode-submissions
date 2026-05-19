class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return res
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i,m):
            if i==len(digits):
                res.append(m)
                return
            for ch in digitToChar[digits[i]]:
                dfs(i+1,m+ch)
                
        dfs(0,"")
        return res

        
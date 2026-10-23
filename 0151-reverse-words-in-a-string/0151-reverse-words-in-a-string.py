class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split(" ")
        mg=''
        for st in x[::-1]:
            if st=='':
                continue
            mg=mg+st+" "
        return mg[:-1]
        
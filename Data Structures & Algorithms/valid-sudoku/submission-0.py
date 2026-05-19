from collections import Counter
class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        for i in range(0,9):
            ele=[num for num in nums[i] if num!='.']
            if len(set(ele))!=len(ele):
                return False
                    

        for i in range(0,9):
            eles=[nums[m][i] for m in range(0,9) if nums[m][i]!='.']
            if len(set(eles))!=len(eles):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                x=[]
                for k in range(3):
                    for l in range(3):
                        if nums[i+k][j+l]!=".":
                            x.append(nums[i+k][j+l])
                if len(set(x))!=len(x):
                    return False
            



        return True 




                    


        
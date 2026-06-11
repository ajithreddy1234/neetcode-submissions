class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        m=[]
        result = {val: idx for idx, val in enumerate(numbers)}
        while l<r:
            summ=numbers[l]+numbers[r]
            if summ==target:
                return [l+1,r+1]
            elif summ<target:
                l+=1
            else:
                r-=1
       



        
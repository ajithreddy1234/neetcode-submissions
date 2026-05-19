class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=[]
        for num in nums:
            if num in temp:
                return True
            temp.append(num)
        return False

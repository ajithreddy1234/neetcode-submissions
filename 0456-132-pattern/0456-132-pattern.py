from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        m=-float("inf")
        stack=[]
        for r in range(len(nums)-1,-1,-1):
            if nums[r]<m:
                return True
            while stack and stack[-1]<nums[r]:
                m=stack.pop()
            stack.append(nums[r])
        return False

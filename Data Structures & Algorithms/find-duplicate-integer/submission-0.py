class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=set()
        for l in nums:
            if l in x:
                return l
            x.add(l)
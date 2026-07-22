class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxx=0
        for r in range(len(nums)):
            if r>maxx:
                return False
            maxx=max(maxx,r+nums[r])  
            if maxx>len(nums)-1:
                return True
        return True

        
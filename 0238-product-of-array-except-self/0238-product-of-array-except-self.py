class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=1
        n=len(nums)
        mg=1
        fin=[1]*n
        for i in range(1,n):
            m*=nums[i-1]
            fin[i]*=m
            mg*=nums[n-i]
            fin[n-i-1]*=mg
        return fin

        
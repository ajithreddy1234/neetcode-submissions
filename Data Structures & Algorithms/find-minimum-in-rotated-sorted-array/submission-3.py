class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[r]
        while l<r:
            if nums[r]>nums[l]:
                return nums[l]
            mid=l+(r-l)//2
            if nums[mid]>res:
                l=mid+1
            else:
                r=mid
                res=nums[r]
        return res

                
        
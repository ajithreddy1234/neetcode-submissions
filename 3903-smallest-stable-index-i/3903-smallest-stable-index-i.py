class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        final=[0]*n
        mi=nums[-1]
        for i in range(n-1,-1,-1):
            if nums[i]<mi:
                mi=nums[i]
            final[i]=mi
        ma=nums[0]
        for i in range(n):
            if nums[i]>ma:
                ma=nums[i]
            final[i]=ma-final[i]
            if final[i]<=k:
                return i
        print(final)
        return -1

        
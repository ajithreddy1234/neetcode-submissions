class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        l=0
        res=[]
        for i in range(k-1,n):
            res.append(max(nums[l:i+1]))
            l+=1
        return res

        
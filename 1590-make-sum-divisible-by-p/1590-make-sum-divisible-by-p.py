class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        sum_nums=sum(nums)
        if sum_nums%p==0:
            return 0
        find=sum_nums//p
        rem=sum_nums%p
        pre={0:-1}
        prefix_sum=0
        ans=float("inf")
        for i in range(len(nums)):
            prefix_sum=(nums[i]+prefix_sum)%p
            target=(prefix_sum-rem)%p
            if target in pre:
                ans=min(ans,i-pre[target])
            pre[prefix_sum]=i
        if ans==len(nums):
            return -1
        return ans if ans!=float("inf") else -1


        
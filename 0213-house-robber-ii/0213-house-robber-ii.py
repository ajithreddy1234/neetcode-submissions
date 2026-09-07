class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def ro(k):
            if len(k)==1:
                return k[0]
            prev1=k[0]
            prev2=max(k[0],k[1])
            for i in range(2,len(k)):
                cur=max(prev1+k[i],prev2)
                prev1=prev2
                prev2=cur
            return max(prev2,prev1)
        return max(ro(nums[1:]),ro(nums[:-1]))
                

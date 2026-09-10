class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        n=len(nums)
        def solve(index,su):
            if index==n:
                return int(su==target)
            if (index,su) in memo:
                return memo[(index,su)]
            neg=solve(index+1,su-nums[index])
            take=solve(index+1,su+nums[index])
            memo[(index,su)]=neg+take
            return memo[(index,su)]
        m=solve(0,0)
        print(memo)
        return m
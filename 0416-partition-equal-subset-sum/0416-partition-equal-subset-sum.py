class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=sum(nums)
        if target%2!=0:
            return False
        else:
            target=target//2
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        def solve(index,current):
            if current==target:
                return True
            if current>target or index<0:
                return False
            if dp[index][current]!=-1:
                return dp[index][current]
            no=solve(index-1,current)
            take=solve(index-1,nums[index]+current)
            dp[index][current]=take or no
            return dp[index][current]
        return solve(len(nums)-1,0)

        
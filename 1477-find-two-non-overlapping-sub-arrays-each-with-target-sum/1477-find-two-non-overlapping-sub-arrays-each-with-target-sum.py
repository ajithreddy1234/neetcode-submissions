class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        l=0
        su=0
        end=[-1]*n
        for r in range(n):
            su+=arr[r]
            while su>target:
                su-=arr[l]
                l+=1
            if su==target:
                end[l]=r
        dp=[[-1 for i in range(3)]for i in range(n+1)]
        def solve(index,rem):
            if rem==0:
                return 0
            if index>=n:
                return float("inf")
            if dp[index][rem]!=-1:
                return dp[index][rem]
            no=solve(index+1,rem)
            take=float("inf")
            if end[index]!=-1:
                j=end[index]
                length=j-index+1
                take=length+solve(j+1,rem-1)
            dp[index][rem]=min(no,take)
            return dp[index][rem]
        m=solve(0,2)
        return m if m!=float("inf") else -1
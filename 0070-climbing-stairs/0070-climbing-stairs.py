class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=1
        prev2=1
        if n==1:
            return prev2
        for i in range(2,n):
            temp=prev1
            prev1=prev1+prev2
            prev2=temp
        return prev1+prev2
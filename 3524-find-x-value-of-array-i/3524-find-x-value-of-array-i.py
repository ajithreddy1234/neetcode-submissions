class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        memo=[None]*n
        def solve(i):
            if i==n:
                return [0]*k
            if memo[i]!=None:
                return memo[i]
            count=[0]*k
            val=nums[i]%k
            count[val]+=1
            nex=solve(i+1)
            for r in range(k):
                c=nex[r]
                mg=(val*r)%k
                count[mg]+=c
            memo[i]=count
            print(count)
            return count
        solve(0)
        final=[0]*k
        for i in range(n):
            for r in range(k):
                final[r]+=memo[i][r]
        return final

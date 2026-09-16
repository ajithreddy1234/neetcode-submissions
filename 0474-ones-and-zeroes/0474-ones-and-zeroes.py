class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        memo={}
        def calc(ele):
            ones=0
            zeros=0
            for e in ele:
                if e=="0":
                    zeros+=1
                elif e=="1":
                    ones+=1
            return zeros,ones
        def solve(index,zero,one):
            if index==len(strs):
                return 0
            if (index,zero,one) in memo:
                return memo[(index,zero,one)]
            no=solve(index+1,zero,one)
            take=0
            zeros,ones=calc(strs[index])
            if zeros+zero<=m and ones+one<=n:
                take=1+solve(index+1,zeros+zero,ones+one)
            memo[(index,zero,one)]=max(take,no)
            return memo[(index,zero,one)]
        return solve(0,0,0)
        return 
        
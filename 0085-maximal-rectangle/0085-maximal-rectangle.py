class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp=matrix[0].copy()
        def maximum(nums):
            res=0
            stack=[]
            for i in range(len(nums)):
                nums[i]=int(nums[i])
                while stack and nums[stack[-1]]>nums[i]:
                    x=stack.pop()
                    if stack:
                        width=i-stack[-1]-1
                    else:
                        width=i
                    res=max(res,nums[x]*width)
                stack.append(i)
            i=i+1
            while stack:
                x=stack.pop()
                if stack:
                    width=i-stack[-1]-1

                else:
                    width=i
                res=max(res,nums[x]*width)
            return res
        mi=maximum(dp)
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="0":
                    dp[j]="0"
                    continue
                dp[j]=str(int(dp[j])+1)
            mi=max(maximum(dp),mi)
        return mi
            
    


        
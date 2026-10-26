class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMax(nums)-self.sumSubarrayMins(nums)
    def sumSubarrayMins(self, arr: list[int]) -> int:
        mg=[0]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if not stack:
                mg[i]=(i+1)*arr[i]
            else:
                mg[i]=(i-stack[-1])*arr[i]+mg[stack[-1]]
            stack.append(i)
        return sum(mg)
    def sumSubarrayMax(self, arr: list[int]) -> int:
        mg=[0]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            if not stack:
                mg[i]=(i+1)*arr[i]
            else:
                mg[i]=(i-stack[-1])*arr[i]+mg[stack[-1]]
            stack.append(i)
        return sum(mg)
         
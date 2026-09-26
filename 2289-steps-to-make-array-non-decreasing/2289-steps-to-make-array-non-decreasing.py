class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack=[]
        mg=0
        for x in nums:
            wait=0
            while stack and stack[-1][1]<=x:
                req,val=stack.pop()
                wait=max(req,wait)
            if stack:
                required_value=wait+1
            else:
                required_value=0
            stack.append((required_value,x))
            mg=max(mg,required_value)
        return mg



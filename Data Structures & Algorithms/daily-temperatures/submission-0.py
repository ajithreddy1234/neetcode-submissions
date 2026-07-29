class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        fin=[0]*len(temperatures)
        for i,val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                x,y=stack.pop()
                fin[x]=i-x
            stack.append([i,val])
        return fin
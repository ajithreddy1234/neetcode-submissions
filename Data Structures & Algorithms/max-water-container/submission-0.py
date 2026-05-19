class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        x=[]
        for i in range(n):
            for j in range(i+1,n):
                m=min(heights[i],heights[j])*(j-i)
                x.append(m)
        return max(x)
            
        
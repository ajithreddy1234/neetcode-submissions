class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=max(heights)
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                res=max(res,(j-i+1)*min(heights[i:j+1]))
        return res
        
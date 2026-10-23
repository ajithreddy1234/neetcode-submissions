class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights = heights + [0]  # Sentinel to process remaining bars
        stack = []
        res = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                x = stack.pop()

                left = stack[-1] if stack else -1
                width = i - left - 1

                res = max(res, heights[x] * width)

            stack.append(i)

        return res
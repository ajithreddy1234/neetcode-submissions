from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Find longest sorted prefix
        left = 0
        while left + 1 < n and nums[left] <= nums[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Find longest sorted suffix
        right = n - 1
        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1

        # Base cases:
        # remove everything after prefix
        # or remove everything before suffix
        ans = min(
            n - left - 1,
            right
        )

        i = 0
        j = right

        # Try joining some prefix with some suffix
        while i <= left and j < n:

            if nums[i] <= nums[j]:
                # nums[i] and nums[j] can connect
                ans = min(ans, j - i - 1)
                i += 1
            else:
                # nums[j] is too small
                j += 1

        return ans
        
        
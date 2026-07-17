class Solution:
    def trap(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 0
        r = len(nums) - 1

        left_max = nums[l]
        right_max = nums[r]

        water = 0

        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, nums[l])
                water += left_max - nums[l]
            else:
                r -= 1
                right_max = max(right_max, nums[r])
                water += right_max - nums[r]

        return water
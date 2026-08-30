class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        mi_ind = nums.index(min(nums))
        ma_ind = nums.index(max(nums))

        left = min(mi_ind, ma_ind)
        right = max(mi_ind, ma_ind)

        # Case 1: Delete both from the left
        delete_left = right + 1

        # Case 2: Delete both from the right
        delete_right = n - left

        # Case 3: Delete one from left and one from right
        delete_both = (left + 1) + (n - right)

        return min(delete_left, delete_right, delete_both)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur_max = max(nums[:k])
        l = 0
        ret = [cur_max]

        for r in range(k, len(nums)):
            if nums[r] >= cur_max:
                cur_max = nums[r]
                ret.append(cur_max)
                l += 1
            else:
                cur_max = max(nums[l + 1 : r + 1])
                ret.append(cur_max)
                l += 1

        return ret
        
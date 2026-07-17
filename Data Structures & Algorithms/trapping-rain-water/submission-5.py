class Solution:
    def trap(self, nums: List[int]) -> int:
        def calc(l, r):
            water_level = min(nums[l], nums[r])
            ans = 0

            for i in range(l + 1, r):
                ans += max(0, water_level - nums[i])

            return ans

        n = len(nums)

        if n < 3:
            return 0

        l = 0
        res = 0

        while l < n - 1:
            r = l + 1

            # Find the first wall at least as tall as nums[l]
            while r < n and nums[r] < nums[l]:
                r += 1

            # If no taller/equal wall exists, use the tallest wall remaining
            if r == n:
                r = l + 1

                for i in range(l + 1, n):
                    if nums[i] > nums[r]:
                        r = i

            if r == l + 1:
                l += 1
            else:
                res += calc(l, r)
                l = r

        return res
from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:
        count = 0
        i = 0
        j = 0
        res = 0

        n = len(nums1) + len(nums2)
        median_sum = 0

        if n % 2 == 0:
            while True:

                # Select the next smallest element
                if i < len(nums1) and (
                    j >= len(nums2) or nums1[i] <= nums2[j]
                ):
                    res = nums1[i]
                    i += 1
                else:
                    res = nums2[j]
                    j += 1

                # Current selected element is at index count
                if count == n // 2 - 1:
                    median_sum = res

                if count == n // 2:
                    return float((median_sum + res) / 2)

                count += 1

        else:
            while True:

                # Select the next smallest element
                if i < len(nums1) and (
                    j >= len(nums2) or nums1[i] <= nums2[j]
                ):
                    res = nums1[i]
                    i += 1
                else:
                    res = nums2[j]
                    j += 1

                if count == n // 2:
                    return float(res)

                count += 1
from typing import List
from functools import cache
from bisect import bisect_right
import sys

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Keep original index
        arr = []
        for i, (start, end, weight) in enumerate(intervals):
            arr.append((start, end, weight, i))

        # Sort according to starting point
        arr.sort()

        n = len(arr)
        starts = [x[0] for x in arr]

        sys.setrecursionlimit(100000)

        @cache
        def solve(index, count):

            # We can take at most 4 intervals
            if index == n or count == 4:
                return (0, ())

            start, end, weight, original_index = arr[index]

            # -------------------------
            # OPTION 1: DON'T TAKE
            # -------------------------
            no_score, no_indices = solve(index + 1, count)

            # -------------------------
            # OPTION 2: TAKE
            # -------------------------

            # Find first interval whose start > current end
            next_index = bisect_right(starts, end)

            future_score, future_indices = solve(
                next_index,
                count + 1
            )

            take_score = weight + future_score

            take_indices = tuple(
                sorted((original_index,) + future_indices)
            )

            # -------------------------
            # Decide better answer
            # -------------------------

            if take_score > no_score:
                return (take_score, take_indices)

            if no_score > take_score:
                return (no_score, no_indices)

            # Same score -> lexicographically smaller list
            if take_indices < no_indices:
                return (take_score, take_indices)

            return (no_score, no_indices)

        score, answer = solve(0, 0)

        return list(answer)
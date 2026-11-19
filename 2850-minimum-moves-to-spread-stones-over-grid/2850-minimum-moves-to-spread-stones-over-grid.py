from functools import cache


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        extras = []
        empty = []

        for r in range(3):
            for c in range(3):
                stones = grid[r][c]
                if stones == 0:
                    empty.append((r, c))
                else:
                    extras.extend([(r, c)] * (stones - 1))

        m = len(empty)
        full_mask = (1 << m) - 1

        @cache
        def dp(mask: int) -> int:
            if mask == full_mask:
                return 0

            i = mask.bit_count()
            r, c = extras[i]
            best = float("inf")

            for j, (x, y) in enumerate(empty):
                bit = 1 << j
                if mask & bit:
                    continue

                distance = abs(r - x) + abs(c - y)
                best = min(best, distance + dp(mask | bit))

            return best

        return dp(0)
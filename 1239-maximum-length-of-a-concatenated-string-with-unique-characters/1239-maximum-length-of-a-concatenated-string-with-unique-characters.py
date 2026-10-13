class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def backtrack(i, taken):
            if i >= len(arr):
                return 0

            # Skip this string
            best = backtrack(i + 1, taken)

            chars = set(arr[i])

            # Reject internal duplicates or overlap with taken
            if len(chars) != len(arr[i]) or chars & taken:
                return best

            # Take this string
            taken.update(chars)
            best = max(
                best,
                len(arr[i]) + backtrack(i + 1, taken)
            )

            # Undo this choice
            taken.difference_update(chars)

            return best

        return backtrack(0, set())
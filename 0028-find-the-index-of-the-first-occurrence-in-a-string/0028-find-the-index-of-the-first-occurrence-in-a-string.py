class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        if not pattern:
            return 0

        # Part 1: Build the LPS array
        m = len(pattern)
        lps = [0] * m

        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1

            elif length > 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

        # Part 2: Search for the pattern
        i = 0  # Pointer in text
        j = 0  # Pointer in pattern

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == m:
                    return i - j

            elif j > 0:
                j = lps[j - 1]

            else:
                i += 1

        return -1
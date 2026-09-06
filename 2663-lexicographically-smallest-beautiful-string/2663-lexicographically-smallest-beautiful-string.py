class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        for i in range(n - 1, -1, -1):

            # Try increasing s[i]
            for val in range(ord(s[i]) - ord('a') + 1, k):

                ch = chr(ord('a') + val)

                if i > 0 and s[i - 1] == ch:
                    continue

                if i > 1 and s[i - 2] == ch:
                    continue

                s[i] = ch

                # Rebuild suffix greedily
                for j in range(i + 1, n):

                    for nxt in range(k):
                        ch2 = chr(ord('a') + nxt)

                        if j > 0 and s[j - 1] == ch2:
                            continue

                        if j > 1 and s[j - 2] == ch2:
                            continue

                        s[j] = ch2
                        break

                return "".join(s)

        return ""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1 = len(str1)
        n2 = len(str2)

        memo = {}

        # STEP 1: Find minimum SCS length
        def solve(i, j):

            if i == n1:
                return n2 - j

            if j == n2:
                return n1 - i

            if (i, j) in memo:
                return memo[(i, j)]

            if str1[i] == str2[j]:

                cost = 1 + solve(i + 1, j + 1)

            else:

                cost1 = 1 + solve(i + 1, j)

                cost2 = 1 + solve(i, j + 1)

                cost = min(cost1, cost2)

            memo[(i, j)] = cost

            return cost

        # Fill the memo with required states
        solve(0, 0)

        # STEP 2: Reconstruct the string
        i = 0
        j = 0

        ans = []

        while i < n1 and j < n2:

            # Case 1: Characters match
            if str1[i] == str2[j]:

                ans.append(str1[i])

                i += 1
                j += 1

            # Case 2: Characters differ
            else:

                cost1 = solve(i + 1, j)
                cost2 = solve(i, j + 1)

                if cost1 <= cost2:

                    ans.append(str1[i])
                    i += 1

                else:

                    ans.append(str2[j])
                    j += 1

        # STEP 3: Append remaining characters
        while i < n1:
            ans.append(str1[i])
            i += 1

        while j < n2:
            ans.append(str2[j])
            j += 1

        return "".join(ans)
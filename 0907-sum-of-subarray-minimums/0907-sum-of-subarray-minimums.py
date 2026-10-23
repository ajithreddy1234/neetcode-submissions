class Solution:
    def findNSE(self, arr: list[int]) -> list[int]:
        n = len(arr)
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            nse[i] = stack[-1] if stack else n
            stack.append(i)

        return nse

    def findPSEE(self, arr: list[int]) -> list[int]:
        n = len(arr)
        psee = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            psee[i] = stack[-1] if stack else -1
            stack.append(i)

        return psee

    def sumSubarrayMins(self, arr: list[int]) -> int:
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)

        total = 0
        mod = 10**9 + 7

        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i

            total = (total + left * right * arr[i]) % mod

        return total
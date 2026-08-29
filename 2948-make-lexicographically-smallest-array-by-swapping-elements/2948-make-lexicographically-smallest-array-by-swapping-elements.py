class Solution:

    def lexicographicallySmallestArray(
        self,
        nums: List[int],
        limit: int
    ) -> List[int]:

        n = len(nums)

        arr = []

        for i in range(n):
            arr.append([nums[i], i])

        arr.sort()

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            indices = []

            for k in range(start, end + 1):
                indices.append(arr[k][1])
            indices.sort()
            print(indices)

            for k in range(len(indices)):
                print(indices[k])
                ans[indices[k]] = arr[start + k][0]

            start = end + 1

        return ans
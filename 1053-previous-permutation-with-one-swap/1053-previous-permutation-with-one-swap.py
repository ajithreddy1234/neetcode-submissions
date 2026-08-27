class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        n = len(arr)

        if n < 2:
            return arr

        # Step 1: Find breakpoint
        i = n - 2

        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        # Already smallest possible permutation
        if i < 0:
            return arr

        # Step 2: Find largest value smaller than arr[i]
        j = n - 1

        while arr[j] >= arr[i]:
            j -= 1

        # Avoid duplicate value:
        # move to leftmost occurrence of arr[j]
        while j > i + 1 and arr[j] == arr[j - 1]:
            j -= 1

        # Step 3: Swap once
        arr[i], arr[j] = arr[j], arr[i]

        return arr
            
        
        
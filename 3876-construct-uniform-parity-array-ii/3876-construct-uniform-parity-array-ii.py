class Solution:
    def uniformArray(self, nums: list[int]) -> bool:

        min_odd = float("inf")
        min_even = float("inf")

        for num in nums:

            if num % 2:
                min_odd = min(min_odd, num)

            else:
                min_even = min(min_even, num)

        # No odd numbers -> all even
        if min_odd == float("inf"):
            return True

        # Otherwise smallest odd must be smaller
        # than smallest even
        return min_odd < min_even

        

                    
                        



        
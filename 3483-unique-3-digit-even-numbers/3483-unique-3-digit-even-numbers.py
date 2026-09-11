from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        count = 0

        for number in range(100, 1000, 2):
            required = Counter(map(int, str(number)))

            if all(required[digit] <= available[digit]
                   for digit in required):
                count += 1

        return count
                    


        
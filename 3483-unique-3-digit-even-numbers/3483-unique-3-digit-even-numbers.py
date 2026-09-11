class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for digit in digits:
            freq[digit] += 1

        count = 0

        for number in range(100, 1000, 2):
            a = number // 100
            b = (number // 10) % 10
            c = number % 10

            freq[a] -= 1
            freq[b] -= 1
            freq[c] -= 1

            if freq[a] >= 0 and freq[b] >= 0 and freq[c] >= 0:
                count += 1

            freq[a] += 1
            freq[b] += 1
            freq[c] += 1

        return count

                    


        
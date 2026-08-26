class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 
        answer = 0 
        frequency = {0: 1}
        for num in nums: 
            prefix_sum += num 
            answer += frequency.get(prefix_sum - k, 0)
            frequency[prefix_sum] = ( frequency.get(prefix_sum, 0) + 1 )
        return answer
        
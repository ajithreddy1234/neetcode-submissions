class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        cur_sum=0
        x=deque()
        for r in range(len(nums)):
            while x and r-x[0][0]>k:
                x.popleft()
            cur_sum=nums[r]+(x[0][1] if x else 0)
            while x and x[-1][1]<cur_sum:
                x.pop()
            x.append([r,cur_sum])
        return cur_sum

        
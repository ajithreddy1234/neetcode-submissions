class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        fin=[]
        dq=deque()
        cur=-1
        for i in range(len(nums)):
            while dq and dq[0]<=cur:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                fin.append(nums[dq[0]])
                cur+=1
        return fin
        
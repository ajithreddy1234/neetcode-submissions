class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        l=-1
        rem=0
        for r in range(len(gas)):
            rem+=gas[r]-cost[r]
            print(rem)
            if rem<0:
                rem=0
                l=-1
            else:
                if l==-1:
                    l=r

            
        return l

            
        
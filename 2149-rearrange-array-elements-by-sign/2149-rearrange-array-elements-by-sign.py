class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        possi=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                possi.append(num)
        final=[]
        for i in range(max(len(possi),len(neg))):
            if i<len(possi):
                final.append(possi[i])
            if i<len(neg):
                final.append(neg[i])
        return final
        


        
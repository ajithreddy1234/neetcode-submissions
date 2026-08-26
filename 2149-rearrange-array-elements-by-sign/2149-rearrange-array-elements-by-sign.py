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
        for i in range(len(possi)):
            final.append(possi[i])
            final.append(neg[i])
        return final


        
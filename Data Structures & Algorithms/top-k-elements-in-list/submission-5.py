class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        x={}
        for num in nums:
            if num in x.keys():
                x[num]+=1
            else:
                x[num]=1
        sort_x=sorted(x.items(),key=lambda x:x[1],reverse=True)
        print(sort_x)
        top_2=[key for key,value in sort_x[:k]]
        return top_2
        
            
        
        
    
        
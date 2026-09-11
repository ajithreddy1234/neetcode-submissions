class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        consi=set()
        n=len(digits)
        s=[]
        visited=set()
        count=0
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range(n):
                if j==i:
                    continue
                for k in range(n):
                    if k==i or k==j:
                        continue
                    x=digits[i]*100+digits[j]*10+digits[k]
                    if digits[k]%2==0 and x not in visited and x>99:
                        visited.add(x)
                        count+=1
                        
        return count


                    


        
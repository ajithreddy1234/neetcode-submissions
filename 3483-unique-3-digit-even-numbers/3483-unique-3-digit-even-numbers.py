class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        consi=set()
        n=len(digits)
        s=[]
        count=0
        visited=set()
        for i in range(n):
            if digits[i]==0:
                continue
            s.append(str(digits[i]))
            for j in range(n):
                if j==i:
                    continue
                s.append(str(digits[j]))
                for k in range(n):
                    if k==i or k==j:
                        continue
                    s.append(str(digits[k]))
                    x=int("".join(s))
                    if digits[k]%2==0 and x not in visited and x>99:
                        print(x)
                        visited.add(x)
                        count+=1
                        s.pop()
                    else:
                        s.pop()
                s.pop()
            s.pop()
        return count


                    


        
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        pr=1
        su=0
        while n>0:
            x=n%10
            pr*=x
            su+=x
            n=n//10
        return original%(su+pr)==0


        
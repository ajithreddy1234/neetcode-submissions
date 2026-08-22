class Solution:
    def checkDivisibility(self, n: int) -> bool:
        su=0
        pr=1
        for m in str(n):
            su+=int(m)
            pr*=int(m)
        return n%(su+pr)==0


        
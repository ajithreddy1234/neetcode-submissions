class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def factorial(i):
            if i==0:
                return 1
            val=1
            for j in range(1,i+1):
                val*=j
            return val
        final=[]
        for i in range(numRows):
            x=[]
            for j in range(i+1):
                v=factorial(i)//(factorial(j)*factorial(i-j))
                x.append(v)
            final.append(x)
        return final


        
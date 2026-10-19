class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        final=[[1]]
        for i in range(numRows-1):
            x=final[-1]
            cur=[]
            cur.append(1)
            for k in range(1,len(x)):
                cur.append(x[k]+x[k-1])
            cur.append(1)
            final.append(cur)
        return final


        
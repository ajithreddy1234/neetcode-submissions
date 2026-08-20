class Solution:
    def maxNumberOfFamilies(self, nn: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        Fi=True
        Se=True
        Th=True
        res=0
        n=len(reservedSeats)
        j=1
        j_check=True
        for i in range(n):
            row=reservedSeats[i][0]
            col=reservedSeats[i][1]
            res += 2 * (row - j)
            j = row
            if 2<=col<=5:
                if Fi:
                    Fi=False
            if 4<=col<=7:
                if Se:
                    Se=False
            if 6<=col<=9:
                if Th:
                    Th=False
            if i+1<n and reservedSeats[i][0]!=reservedSeats[i+1][0]:
                if Fi and Se and Th:
                    res+=2
                elif (Fi and Se) or (Se and Th) or (Fi and Th) or Fi or Th or Se:
                    res+=1
                Fi=True
                Se=True
                Th=True
                j+=1
            if i+1==n:
                res += 2 * (nn - reservedSeats[i][0])
                if Fi and Se and Th:
                    res+=2
                elif (Fi and Se) or (Se and Th) or (Th and Fi) or Fi or Th or Se:
                    res+=1
                Fi=True
                Se=True
                Th=True
        return res

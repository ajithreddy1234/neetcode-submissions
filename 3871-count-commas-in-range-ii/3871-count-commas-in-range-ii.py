class Solution:
    def countCommas(self, n: int) -> int:
        if n<10**3:
            return 0
        if n<10**6:
            return n-999
        if n<10**9:
            return 999000+(n-10**6+1)*2
        if n<10**12:
            return 999000+999000000*2+(n-10**9+1)*3
        if n<10**15:
            return 999000+999000000*2+999000000000*3+(n-10**12+1)*4
        if n==10**15:
            return 999000+999000000*2+999000000000*3+999000000000000*4+5



        
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        dp=[[float("inf") for i in range(n2+1)] for i in range(n1+1)]
        def solve(i,j):
            if i>=n1:
                return n2-j
            elif j>=n2:
                return n1-i
            if dp[i][j]!=float("inf"):
                return dp[i][j]
            if str1[i]==str2[j]:
                cost=1+solve(i+1,j+1)
            else:
                cost1=1+solve(i+1,j)
                cost2=1+solve(i,j+1)
                if cost1<=cost2:
                    cost=cost1
                else:
                    cost=cost2
            dp[i][j]=cost
            return cost
        solve(0,0)
        i=0
        j=0
        fin=[]
        while i<n1 and j<n2:
            if str1[i]==str2[j]:
                fin.append(str1[i])
                i+=1
                j+=1
            else:
                cost1=dp[i+1][j]
                cost2=dp[i][j+1]
                if cost1<=cost2:
                    fin.append(str1[i])
                    i+=1
                else:
                    fin.append(str2[j])
                    j+=1
        print(fin)
        while i<n1:
            fin.append(str1[i])
            i+=1
        while j<n2:
            fin.append(str2[j])
            j+=1
        return "".join(fin)
        

                    

        

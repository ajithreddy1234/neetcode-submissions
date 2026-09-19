class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        dp=[[0 for i in range(n2+1)] for i in range(n1+1)]
        for i in range(n2):
            dp[n1][i]=n2-i
        for j in range(n1):
            dp[j][n2]=n1-j
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if str1[i]==str2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j],dp[i][j+1])
        print(dp)
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
        

                    

        

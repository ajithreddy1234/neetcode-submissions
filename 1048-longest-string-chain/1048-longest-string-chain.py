class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda x:len(x))
        print(words)
        n=len(words)
        def lc(s1,s2):
            n1=len(s1)
            n2=len(s2)
            j=0
            for i in range(n2):
                if j==n1:
                    return True
                if s2[i]==s1[j]:
                    j+=1
            if j==n1:
                return True
            return False
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if len(words[i])+1==len(words[j]) and lc(words[i],words[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

                    
                
            
        
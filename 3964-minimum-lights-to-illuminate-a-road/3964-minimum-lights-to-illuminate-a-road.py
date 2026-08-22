class Solution:
    def minLights(self, lights: list[int]) -> int:
        final=[]
        n=len(lights)
        left_end=False
        right_end=False
        for i in range(len(lights)):
            if lights[i]==0:
                continue
            else:
                left=max(0,i-lights[i])
                right=min(n-1,i+lights[i])
                if left==0:
                    left_end=True
                if right==n-1:
                    right_end=True
                if final and final[-1][1]>=left:
                    x,y=final.pop()
                    final.append([min(left,x),max(right,y)])
                else:
                    final.append([left,right])
        if len(final)==0:
            return math.ceil(n/3)
        else:
            ans=0
            m=len(final)
            print(final,left_end,right_end)
            if not left_end:
                ans+=ceil(final[0][0]/3)
                print(ans,0)
            if not right_end:
                ans+=ceil((n-1-final[-1][1])/3)
            if m>=2:
                for i in range(1,m):
                    if (final[i][0]-final[i-1][1])>0:
                        ans+=ceil((final[i][0]-final[i-1][1]-1)/3)
                        print(final[i],final[i-1],ans,2)
            return ans

                    
        
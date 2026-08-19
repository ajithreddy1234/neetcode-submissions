class Solution:
    def reorganizeString(self, s: str) -> str:
        counter=Counter(s)
        some=[]
        for key,value in counter.items():
            some.append([value,key])
        some.sort(reverse=True)
        some=deque(some)
        final=''
        while some:
            if len(some)==1 and some[0][0]>1:
                return ""
            final+=some[0][1]
            some[0][0]-=1
            if some[0][0]!=0:
                i=0
                while i+1<len(some):
                    some[i],some[i+1]=some[i+1],some[i]
                    if some[i][0]<some[i+1][0]:
                        break
                    i+=1      
            else:
                some.popleft()
        return final






        
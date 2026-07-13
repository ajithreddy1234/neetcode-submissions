class TimeMap:

    def __init__(self):
        self.me={}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.me:
            self.me[key]=[]
        self.me[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        l=0 
        if key not in self.me:
            return ""
        r=len(self.me[key])-1
        res=""
        while l<=r:
            m=l+(r-l)//2
            if self.me[key][m][0]<=timestamp:
                res=self.me[key][m][1]
                l=m+1
            else:
                r=m-1
        return res
        


        

class MinStack:
    def __init__(self):
        self.li=[] 
        self.res=[]
    def push(self, val: int) -> None:
        self.li.append(val)
        val=min(val,self.res[-1] if self.res else val)
        self.res.append(val)
        
    def pop(self) -> None:
        self.li.pop()
        self.res.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return self.res[-1]
        

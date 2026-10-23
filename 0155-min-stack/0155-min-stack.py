class MinStack:
    def __init__(self):
        self.li=[] 
        self.res=[]
    def push(self, val: int) -> None:
        self.li.append(val)
        if  self.res and self.res[-1]>=val:
            self.res.append(val)
        elif not self.res:
            self.res.append(val)
        
    def pop(self) -> None:
        x=self.li.pop()
        if x==self.res[-1]:
            self.res.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return self.res[-1]
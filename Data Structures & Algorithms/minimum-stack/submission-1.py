class MinStack:

    def __init__(self):
        self.li=[] 
        self.res=-float("inf")

    def push(self, val: int) -> None:
        self.li.append(val)
        self.res=min(self.res,val)
        
    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return min(self.li)
        

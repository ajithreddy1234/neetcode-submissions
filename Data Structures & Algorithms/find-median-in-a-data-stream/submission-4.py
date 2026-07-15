class MedianFinder:

    def __init__(self):
        self.me=[]

    def addNum(self, num: int) -> None:
        self.me.append(num)

    def findMedian(self) -> float:
        self.me.sort()
        if len(self.me)%2==0:
            return (self.me[len(self.me)//2-1]+self.me[len(self.me)//2])/2
        else:
            return self.me[len(self.me)//2]
        
        
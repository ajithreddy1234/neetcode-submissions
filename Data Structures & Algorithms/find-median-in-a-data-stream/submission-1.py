class MedianFinder:

    def __init__(self):
        self.a=[]
        

    def addNum(self, num: int) -> None:
        self.a.append(num)
        

    def findMedian(self) -> float:
        self.a.sort()
        x=len(self.a)
        if x==1:
            return self.a[0]
        elif x%2!=0:
            return self.a[x//2]
        else:
            return (self.a[x//2]+self.a[x//2-1])/2
        
        
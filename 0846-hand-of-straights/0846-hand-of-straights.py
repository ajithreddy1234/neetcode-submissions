class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        xh=hand[:]
        heapq.heapify(hand)
        x=0
        m=[]
        xy=[]
        while len(hand)>0:
            mg=heapq.heappop(hand)
            if m and m[-1]==mg:
                xy.append(mg)
            elif not m:
                m.append(mg)
            elif mg==m[-1]+1:
                m.append(mg)
            else:
                return False
            if len(m)==groupSize:
                x+=1
                m=[]
                if xy:
                    for num in xy:
                        heapq.heappush(hand,num)
                xy=[]
        if len(m)!=0:
            return False
        return x*groupSize==len(xh)
        


        
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        hand.sort()
        x=Counter(hand)
        for num in hand:
            if x[num]:
                for i in range(num,num+groupSize):
                    if not x[i]:
                        return False
                    x[i]-=1
        return True


        
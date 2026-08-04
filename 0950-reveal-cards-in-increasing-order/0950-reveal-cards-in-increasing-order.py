class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        x=sorted(deck)
        final=[0]*len(deck)
        check=deque([i for i in range(len(deck))])
        l=0
        while check:
            m=check.popleft()
            if check:
                n=check.popleft()
                check.append(n)
            final[m]=x[l]
            l+=1
        return final
            
        
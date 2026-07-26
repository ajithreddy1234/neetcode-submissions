class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=False
        b=False
        c=False
        for r in range(len(triplets)):
            if triplets[r][0]==target[0]:
                if triplets[r][1]<=target[1] and triplets[r][2]<=target[2]:
                    print(triplets[r])
                    a=True
            if triplets[r][1]==target[1]:
                if triplets[r][0]<=target[0] and triplets[r][2]<=target[2]:
                    print(triplets[r])
                    b=True
            if triplets[r][2]==target[2]:
                if triplets[r][0]<=target[0] and triplets[r][1]<=target[1]:
                    print(triplets[r])
                    c=True
        return a and b and c


        
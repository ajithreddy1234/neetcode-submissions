class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        nums.sort()
        def checkodd():
            odds=[]
            for num in nums:
                if num%2!=0:
                    print(num)
                    odds.append(num)
                elif num%2==0:
                    print(num)
                    if not odds:
                        print(0)
                        return False
                    elif odds and odds[-1]<num:
                        continue
                    elif len(odds)>1 and odds[-1]==num:
                        continue
                    elif len(odds)<=1 and odds[-1]==num:
                        print(1)
                        return False
            return True
        def checkeven():
            even=[]
            for num in nums:
                if num%2==0:
                    even.append(num)
                elif num%2!=0:
                    return False
            return True
        if checkeven():
            return True
        elif checkodd():
            return True
        else:
            return False

        

                    
                        



        
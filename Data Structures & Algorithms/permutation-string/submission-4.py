class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
        l = 0
        
        for r in range( len(s2)):
            index1 = ord(s2[r]) - ord('a')
            s2Count[index1] += 1
            if (r - l+1) > len(s1):
                index2 = ord(s2[l]) - ord('a')
                s2Count[index2] -= 1
                l+=1
            if s1Count==s2Count:
                return True
            
        return False











        
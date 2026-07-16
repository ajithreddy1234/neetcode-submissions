class Solution:
    def isPalindrome(self, nums: str) -> bool:
        l=0
        r=len(nums)-1
        while l<r:
            while l<r and not nums[l].isalnum():
                l+=1
            while l<r and not nums[r].isalnum():
                r-=1
            if nums[l].lower()==nums[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
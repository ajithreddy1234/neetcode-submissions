class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for m in s:
            if m.isalpha() or m.isdigit():
                new+=m.lower()
            else:
                continue
        return new==new[::-1]
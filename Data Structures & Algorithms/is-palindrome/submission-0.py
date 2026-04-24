class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        
        return s == s[::-1]
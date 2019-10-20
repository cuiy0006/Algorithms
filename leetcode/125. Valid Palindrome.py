class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        def is_valid(c):
            return c.isdigit() or c.isalpha() 
        
        while i < j:
            while i < j and not is_valid(s[i]):
                i += 1
            
            while i < j and not is_valid(s[j]):
                j -= 1
                
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True
            
            
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = [c for c in s if c.isdigit() or c.isalpha()]
        return lst == lst[::-1]

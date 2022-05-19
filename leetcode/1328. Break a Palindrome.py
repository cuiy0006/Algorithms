class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        is_odd = len(palindrome) % 2 == 1
        mid = len(palindrome) // 2
        i = 0
        while i < len(palindrome):
            if is_odd and i == mid:
                i += 1
                continue
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            i += 1
        
        return palindrome[:-1] + 'b'

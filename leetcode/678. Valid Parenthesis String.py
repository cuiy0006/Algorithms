class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        left_ast = 0
        
        for c in s:
            if c == '(':
                left += 1
            else:
                left -= 1
            
            if c == '(' or c == '*':
                left_ast += 1
            else:
                left_ast -= 1
            
            if left_ast < 0:
                return False
            
            left = max(left, 0)
        
        return left == 0

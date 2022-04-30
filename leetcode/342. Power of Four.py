class Solution:
    def __init__(self):
        curr = 1
        self.s = set()
        max_val = 2 ** 31 - 1
        while curr <= max_val:
            self.s.add(curr)
            curr *= 4
            
    
    def isPowerOfFour(self, n: int) -> bool:
        return n in self.s

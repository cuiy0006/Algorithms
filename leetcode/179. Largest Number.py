import functools

class Num:
    def __init__(self, num):
        self.s = str(num)
    
    def __lt__(self, other):
        return self.s + other.s > other.s + self.s

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        o_lst = [Num(num) for num in nums]
        o_lst.sort()
        if all([o.s == '0' for o in o_lst]):
            return '0'
        return ''.join([o.s for o in o_lst])

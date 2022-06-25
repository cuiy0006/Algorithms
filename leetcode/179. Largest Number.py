class Element:
    def __init__(self, num):
        self.num = str(num)
    
    def __lt__(self, other):
        return self.num + other.num >= other.num + self.num


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        elements = [Element(num) for num in nums]
        elements.sort()
        res = ''.join([element.num for element in elements])
        
        return str(int(res))

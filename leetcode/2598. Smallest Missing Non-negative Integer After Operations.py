class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        dic = {}
        for num in nums:
            m = num % value
            if m < 0:
                m += value
            if m not in dic:
                dic[m] = 0
            dic[m] += 1
        
        num = 0
        while num < len(nums):
            m = num % value
            if m not in dic:
                return num
            dic[m] -= 1
            if dic[m] == 0:
                del dic[m]
            num += 1
        return num

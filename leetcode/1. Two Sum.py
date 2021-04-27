class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in dic:
                return [i, dic[num2]]
            dic[num] = i
        
        return []

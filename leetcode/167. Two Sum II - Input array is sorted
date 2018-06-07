class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1





class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,num in enumerate(numbers):
            dic[target - num] = i
        
        for i,num in enumerate(numbers):
            if num in dic and dic[num] != i:
                return [i+1, dic[num]+1]

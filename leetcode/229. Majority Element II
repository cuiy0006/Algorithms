class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        first = None
        fcnt = 0
        second = None
        scnt = 0
        for num in nums:
            if first == num:
                fcnt += 1
            elif second == num:
                scnt += 1
            elif first is None:
                first = num
                fcnt = 1
            elif second is None:
                second = num
                scnt = 1
            else:
                if fcnt >0:
                    fcnt -= 1
                    if fcnt == 0:
                        first = None
                if scnt > 0:
                    scnt -= 1
                    if scnt == 0:
                        second = None
        lst = []
        if nums.count(first) > n:
            lst.append(first)
        if nums.count(second) > n:
            lst.append(second)
        return lst
                

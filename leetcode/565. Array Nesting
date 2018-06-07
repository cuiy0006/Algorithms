class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        n = len(nums)
        maxval = 0
        for num in nums:
            s = set()
            tmp = num
            
            base = 0
            while tmp < n:
                if tmp in s:
                    break
                if tmp in dic:
                    base = dic[tmp] + 1
                    break
                s.add(tmp)
                tmp = nums[tmp]
                base += 1

            for num in s:
                dic[num] = base
            if len(s) != 0:
                maxval = max(maxval, base)
        return maxval

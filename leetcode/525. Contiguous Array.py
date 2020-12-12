class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        dic = {0:-1}
        maxlen = 0
        for i, num in enumerate(nums):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in dic:
                maxlen = max(maxlen, i - dic[cnt])
            else:
                dic[cnt] = i
        return maxlen

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        dic = {num:0 for num in nums}
        for num in nums:
            tmp = num
            while tmp in dic:
                if dic[tmp] == 0:
                    tmp -= 1
                else:
                    break
            if tmp not in dic:
                cnt = 1
                for i in range(tmp+1, num+1):
                    dic[i] = cnt
                    cnt += 1
            else:
                for i in range(tmp+1, num+1):
                    dic[i] = dic[i-1] + 1
            maxlen = max(maxlen, dic[num])
        return maxlen

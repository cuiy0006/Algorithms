class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        cnt = 0
        i, j = 0, 0
        maxlen = 0
        while j < len(s):
            if s[j] in dic:
                if dic[s[j]] == 0:
                    cnt += 1
            else:
                cnt += 1
            dic[s[j]] = dic.get(s[j], 0) + 1
            if cnt > 2:
                maxlen = max(maxlen, j-i)
            while cnt > 2:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    cnt -= 1
                i += 1
            j += 1
        return max(maxlen, j - i)

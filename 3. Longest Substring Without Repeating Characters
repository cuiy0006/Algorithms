class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        i = 0
        j = 0
        max_len = 0
        while i <len(s):
            if s[i] in dic:
                index = dic[s[i]]
                while j <= index:
                    del dic[s[j]]
                    j += 1
            dic[s[i]] = i
            max_len = max(max_len, i - j + 1)
            i += 1
            
        return max_len

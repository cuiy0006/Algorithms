class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(start, end):
            while start >=0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return (start + 1, end - 1)
        
        left = right = 0
        for i in range(len(s)):
            start, end = helper(i, i)
            if end - start >= right - left:
                left, right = start, end
            start, end = helper(i, i + 1)
            if end - start >= right - left:
                left, right = start, end
        return s[left:right+1]
                

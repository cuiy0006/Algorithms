class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt[0] += 1
                left -= 1
                right += 1
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        return cnt[0]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = 0
        def find_edge(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1
        
        for i in range(len(s)):
            left, right = find_edge(i, i)
            if right - left > r - l:
                l = left
                r = right
            if i != 0:
                left, right = find_edge(i - 1, i)
                if right - left > r - l:
                    l = left
                    r = right
        return s[l: r + 1]

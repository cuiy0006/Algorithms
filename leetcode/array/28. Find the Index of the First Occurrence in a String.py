class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        def get_num(c):
            return ord(c) - ord('a')

        target = 0
        n = len(needle)
        for i in range(n):
            target = target * 26 + get_num(needle[i])
        
        curr = 0
        for i in range(n):
            curr = curr * 26 + get_num(haystack[i])
        if curr == target:
            return 0

        for i in range(1, len(haystack)-n+1):
            curr = (curr - get_num(haystack[i-1]) * 26 ** (n-1)) * 26 + get_num(haystack[i+n-1])
            if curr == target:
                return i
        return -1

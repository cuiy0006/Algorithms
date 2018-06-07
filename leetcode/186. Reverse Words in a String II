class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(j, i-1)
                j = i + 1
            elif i == len(s) -1:
                reverse(j, i)
        reverse(0, len(s)-1)

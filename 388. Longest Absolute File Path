class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxLen = 0
        dic = {}
        depth = 0
        curr = ''
        i = 0
        while i < len(input):
            c = input[i]
            if c != '\n' and i != len(input)-1:
                curr += c
            else:
                if i == len(input) - 1:
                    curr += c
                if '.' in curr:
                    length = len(curr)
                    for j in range(depth):
                        length += dic[j] + 1
                    maxLen = max(maxLen, length)
                else:
                    dic[depth] = len(curr)
                curr = ''
                depth = 0
                while i + 1 < len(input) and input[i+1] == '\t':
                    i += 1
                    depth += 1
            i += 1
        return maxLen

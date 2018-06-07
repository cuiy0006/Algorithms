class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i, c1 in enumerate(num1[::-1]):
            for j, c2 in enumerate(num2[::-1]):
                pos = i + j
                tmp = (ord(c1) - ord('0')) * (ord(c2) - ord('0')) + res[pos]
                q = tmp // 10
                r = tmp % 10
                res[pos] = r
                res[pos + 1] += q
        res = res[::-1]
        for i, val in enumerate(res):
            if val != 0:
                res = res[i:]
                break
        return ''.join(map(str, res))
        

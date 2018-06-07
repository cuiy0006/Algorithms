class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c not in dic:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if dic[left] != c:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

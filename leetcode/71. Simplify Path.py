class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        curr = ''
        for i, c in enumerate(path):
            if c == '/':
                if curr != '':
                    if curr == '..':
                        if len(stack) > 0:
                            stack.pop()
                    elif curr != '.':
                        stack.append(curr)
                    curr = ''
            else:
                curr += c
        if curr != '':
            if curr == '..':
                if len(stack) > 0:
                    stack.pop()
            elif curr != '.':
                stack.append(curr)
        return '/' + '/'.join(stack)

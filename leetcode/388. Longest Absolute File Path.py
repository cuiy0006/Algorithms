class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        lst = input.split('\n')
        res = 0
        
        for i in range(len(lst)):
            path = lst[i]
            path_lst = path.split('\t')
            level = len(path_lst)-1
            while len(stack) > level:
                stack.pop()
            stack.append(path_lst[-1])
            if '.' in path:
                s = '/'.join(stack)
                res = max(res, len(s))
        
        return res

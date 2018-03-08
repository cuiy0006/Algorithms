class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def helper(index, path, total, last_curr):
            if index == len(num):
                if total ==target:
                    res.append(path)
                return
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break
                sub = num[index:i+1]
                curr = int(sub)
                if index == 0:
                    helper(i + 1, sub, curr, curr)
                else:
                    helper(i + 1, path + '+' + sub, total + curr, curr)
                    helper(i + 1, path + '-' + sub, total - curr, -curr)
                    helper(i + 1, path + '*' + sub, total - last_curr + last_curr * curr, curr * last_curr)
        helper(0, '', 0, '0')
        return res
                    

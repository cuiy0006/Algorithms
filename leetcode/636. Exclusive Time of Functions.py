class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if len(logs) == 0:
            return []
        res = [0] * n
        stack = []
        for log in logs:
            lst = log.split(':')
            if lst[1] == 'start':
                lst.append(0)
                stack.append(lst)
            else:
                funcid, status, time, minus = stack.pop()
                interval = int(lst[2]) - int(time) + 1
                res[int(funcid)] += interval - minus
                if len(stack) != 0:
                    stack[-1][-1] += interval
        return res
                    

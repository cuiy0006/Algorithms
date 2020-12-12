from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(element):
            cnt = 0
            for c in element:
                if c== '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        q = deque([s])
        res = []
        visited = set()
        maxlen = 0
        
        while len(q) != 0:
            element = q.popleft()
            if len(element) < maxlen:
                break
            if isValid(element):
                res.append(element)
                maxlen = len(element)
                continue
            for i,c in enumerate(element):
                if c != '(' and c != ')':
                    continue
                sub = element[:i] + element[i+1:]
                if sub in visited:
                    continue
                visited.add(sub)
                q.append(sub)
        return res
                

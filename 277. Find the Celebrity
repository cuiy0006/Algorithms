# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
from collections import deque

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        q = deque([i for i in range(n)])
        while len(q) > 1:
            A = q.popleft()
            B = q.popleft()
            AknowB = knows(A, B)
            BknowA = knows(B, A)
            if AknowB and not BknowA:
                q.append(B)
            if BknowA and not AknowB:
                q.append(A)
        if len(q) == 0:
            return -1
        celebrity = q.popleft()
        for i in range(n):
            if celebrity == i:
                continue
            if knows(celebrity, i) or not knows(i, celebrity):
                return -1
        return celebrity

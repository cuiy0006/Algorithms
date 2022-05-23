# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depths = []
        max_depth = 0
        def dfs(lst, depth):
            nonlocal max_depth
            
            for ni in lst:
                if ni.isInteger():
                    depths.append((depth, ni.getInteger()))
                    max_depth = max(max_depth, depth)
                else:
                    dfs(ni.getList(), depth + 1)
        
        dfs(nestedList, 1)
        
        return sum([(max_depth - depth + 1) * val for depth, val in depths])
    
    
    
    
    
    
from collections import deque

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        lst = []
        q = deque(nestedList)
        depth = 1
        while len(q) != 0:
            size = len(q)
            curr = [0, depth]
            for _ in range(size):
                ni = q.popleft()
                if ni.isInteger():
                    curr[0] += ni.getInteger()
                else:
                    q.extend(ni.getList())
            lst.append(curr)
            depth += 1

        max_depth = depth-1
        return sum([num * (max_depth-depth+1) for num, depth in lst])
    
    
    


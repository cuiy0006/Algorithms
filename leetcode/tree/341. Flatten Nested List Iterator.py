# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [(nestedList, 0)]
        self.ni = None
    
    def next(self) -> int:
        return self.ni.getInteger()
    
    def hasNext(self) -> bool:
        while len(self.stack) != 0:
            nl, idx = self.stack.pop()
            if idx > len(nl) - 1:
                continue
            ni = nl[idx]
            if ni.isInteger():
                self.stack.append((nl, idx+1))
                self.ni = ni
                return True
            else:
                self.stack.append((nl, idx+1))
                self.stack.append((ni.getList(), 0))
        if self.ni is None:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
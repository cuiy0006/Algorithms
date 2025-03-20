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
        self.stack = [(0, nestedList)]
    
    def next(self) -> int:
        idx, nl = self.stack.pop()
        if idx+1 < len(nl):
            self.stack.append((idx+1, nl))
        return nl[idx].getInteger()
    
    def hasNext(self) -> bool:
        while len(self.stack) != 0:
            idx, nl = self.stack.pop()
            ni = nl[idx]
            if ni.isInteger():
                self.stack.append((idx, nl))
                break
            else:
                if idx+1 < len(nl):
                    self.stack.append((idx+1, nl))
                if len(ni.getList()) != 0:
                    self.stack.append((0, ni.getList()))
        return len(self.stack) != 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




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

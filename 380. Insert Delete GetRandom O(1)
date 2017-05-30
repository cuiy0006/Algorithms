import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.lst = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        idx, last_idx = self.dic[val], len(self.lst)-1
        tmp = self.lst[-1]
        self.lst[idx], self.lst[last_idx], self.dic[tmp] = self.lst[last_idx], self.lst[idx], idx
        self.lst.pop()
        del self.dic[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.lst[random.randint(0, len(self.lst) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

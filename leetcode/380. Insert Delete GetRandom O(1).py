from random import randint

class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.dic[val] = len(self.lst)
            self.lst.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            idx = self.dic[val]
            swapped_val = self.lst[-1]
            self.dic[swapped_val] = idx
            self.lst[idx] = swapped_val
            
            self.lst.pop()
            del self.dic[val]
            
            return True

    def getRandom(self) -> int:
        idx = randint(0, len(self.lst) - 1)
        return self.lst[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

from random import randint

class RandomizedCollection:

    def __init__(self):
        self.dic = {} # val: deque[idx]
        self.lst = [] # [val]

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = set([len(self.lst)])
            self.lst.append(val)
            return True
        else:
            self.dic[val].add(len(self.lst))
            self.lst.append(val)
            return False

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        idx = next(iter(self.dic[val]))
        self.dic[val].remove(idx)
        if len(self.dic[val]) == 0:
            del self.dic[val]
        
        last_idx = len(self.lst) - 1
        last_val = self.lst.pop()
        
        if last_idx == idx:
            return True
        
        self.dic[last_val].remove(last_idx)
        self.dic[last_val].add(idx)
        self.lst[idx] = last_val

        return True

    def getRandom(self) -> int:
        chosen = randint(0, len(self.lst)-1)
        return self.lst[chosen]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

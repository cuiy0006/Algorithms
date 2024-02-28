class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            i = self.dic[val]
            self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
            self.arr.pop()
            del self.dic[val]
            if i != len(self.arr):
                self.dic[self.arr[i]] = i
            return True
        else:
            return False

    def getRandom(self) -> int:
        i = randint(0, len(self.arr)-1)
        return self.arr[i]

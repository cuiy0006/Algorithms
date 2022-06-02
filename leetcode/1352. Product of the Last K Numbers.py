class ProductOfNumbers:

    def __init__(self):
        self.lst = [1]
        self.curr = 1

    def add(self, num: int) -> None:
        if num == 0:
            i = len(self.lst)-1
            while i >= 0:
                if self.lst[i] == 0:
                    break
                self.lst[i] = 0
                i -= 1
            self.lst.append(0)
            self.curr = 1
        else:
            self.curr *= num
            self.lst.append(self.curr)
            

    def getProduct(self, k: int) -> int:
        if self.lst[len(self.lst)-k] == 0:
            return 0
        
        num = self.lst[len(self.lst)-k-1]
        if num == 0:
            num = 1
        
        return self.curr // num

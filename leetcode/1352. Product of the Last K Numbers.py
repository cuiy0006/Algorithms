class ProductOfNumbers:

    def __init__(self):
        self.zero_idx = -1
        self.premultiply = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_idx = len(self.premultiply)
            self.premultiply.append(1)
        else:
            self.premultiply.append(num * self.premultiply[-1])

    def getProduct(self, k: int) -> int:
        r = len(self.premultiply)-1
        l = r-k
        if self.zero_idx > l:
            return 0
        return self.premultiply[r] // self.premultiply[l]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

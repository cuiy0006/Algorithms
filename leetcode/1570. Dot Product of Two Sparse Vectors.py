class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.dic[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if len(self.dic) < len(vec.dic):
            short = self.dic
            long = vec.dic
        else:
            short = vec.dic
            long = self.dic

        for i in short:
            if i in long:
                res += long[i] * short[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
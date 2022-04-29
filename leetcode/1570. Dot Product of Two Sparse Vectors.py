class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_to_num = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.idx_to_num[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        keys1 = set(self.idx_to_num)
        keys2 = set(vec.idx_to_num)
        keys = keys1 & keys2
        
        res = 0
        for key in keys:
            res += self.idx_to_num[key] * vec.idx_to_num[key]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

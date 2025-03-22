class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, nums, merge):
        self.merge = merge
        self.root = self._build(nums, 0, len(nums)-1)

    def _build(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)
        mid = (l+r)//2
        left = self._build(nums, l, mid)
        right = self._build(nums, mid+1, r)
        val = self.merge(left.val, right.val)
        node = Node(val, l, r)
        node.left = left
        node.right = right
        return node
    
    def update(self, idx, val):
        self._update(idx, val, self.root)
    
    def _update(self, idx, val, node):
        if node.l == node.r and idx == node.l:
            node.val = val
            return
        mid = (node.l+node.r)//2
        if idx <= mid:
            self._update(idx, val, node.left)
        else:
            self._update(idx, val, node.right)
        node.val = self.merge(node.left.val, node.right.val)
    
    def query(self, l, r):
        return self._query(l, r, self.root)
    
    def _query(self, l, r, node):
        if node.r == r and node.l == l:
            return node.val
        mid = (node.l+node.r)//2
        if r <= mid:
            return self._query(l, r, node.left)
        elif l > mid:
            return self._query(l, r, node.right)
        else:
            return self.merge(
                self._query(l, mid, node.left),
                self._query(mid+1, r, node.right)
            )

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums, lambda x,y: x+y)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

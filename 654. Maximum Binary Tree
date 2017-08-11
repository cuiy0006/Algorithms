class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxval = max(nums)
        idx = nums.index(maxval)
        node = TreeNode(maxval)
        left = nums[:idx]
        right = nums[idx+1:]
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node

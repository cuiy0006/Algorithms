class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        dic = {0: 1} # sum -> count
        def helper(node, total):
            if node == None:
                return 0
            res = 0
            if (total + node.val - sum) in dic:
                res += dic[total + node.val - sum] 
            
            total += node.val
            if total not in dic:
                dic[total] = 1
            else:
                dic[total] += 1
                
            res += helper(node.left, total) + helper(node.right, total)
            dic[total] -= 1
            return res
        
        return helper(root, 0)

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun minDepth(root: TreeNode?): Int {
        var min_depth = Int.MAX_VALUE
        fun dfs(node: TreeNode?, depth: Int) {
            if (node == null) return
            if (depth >= min_depth) return
            if (node.left == null && node.right == null) {
                min_depth = depth
            }
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        }
        dfs(root, 1)
        return if (min_depth == Int.MAX_VALUE) return 0 else min_depth
    }
}

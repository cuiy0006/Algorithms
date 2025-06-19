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
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val res = mutableListOf<MutableList<Int>>()
        if (root == null) return res

        fun traverse(node: TreeNode?, remain: Int, path: MutableList<Int>) {
            if (node == null) return
            val remain: Int = remain - node.`val`
            path.add(node.`val`)
            if (remain == 0 && node.left == null && node.right == null) {
                res.add(path.toMutableList())
            }
            traverse(node.left, remain, path)
            traverse(node.right, remain, path)
            path.removeLast()
        }
        traverse(root, targetSum, mutableListOf<Int>())

        return res
    }
}

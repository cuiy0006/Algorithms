class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val res = mutableListOf<String>()
        fun generate(left: Int, right: Int, curr: String) {
            if (left == 0 && right == 0) {
                res.add(curr)
                return
            }
            if (left < right) {
                generate(left, right-1, curr + ")")
            }
            if (left > 0) {
                generate(left-1, right, curr + "(")
            }
        }

        generate(n, n, "")
        return res
    }
}

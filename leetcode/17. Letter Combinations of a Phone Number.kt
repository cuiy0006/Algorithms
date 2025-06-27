val keyboard: Map<Char, String> = mapOf(
    '2' to "abc",
    '3' to "def",
    '4' to "ghi",
    '5' to "jkl",
    '6' to "mno",
    '7' to "pqrs",
    '8' to "tuv",
    '9' to "wxyz")

class Solution {
    fun letterCombinations(digits: String): List<String> {
        val res = mutableListOf<String>()
        if (digits.length == 0) return res
        fun getCombinations(idx: Int, curr: MutableList<Char>) {
            if (idx == digits.length) {
                res.add(curr.joinToString(""))
                return
            }
            for (c in keyboard[digits[idx]]!!) {
                curr.add(c)
                getCombinations(idx+1, curr)
                curr.removeLast()
            }
        } 
        getCombinations(0, mutableListOf<Char>())
        return res
    }
}

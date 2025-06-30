class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        fun isValid(s: String): Boolean {
            var left = 0
            for (c in s) {
                when (c) {
                    '(' -> left++
                    ')' -> left--
                }
                if (left < 0) return false
            }
            return left == 0
        }
        val dq = ArrayDeque<String>(listOf(s))
        val visited = mutableSetOf<String>(s)
        val res = mutableListOf<String>()
        while (dq.size != 0) {
            val s = dq.removeFirst()
            if (res.size != 0 && s.length < res[0].length) break
            if (isValid(s)) {
                res.add(s)
                continue
            }
            for (i in 0..s.length-1) {
                val sub = s.substring(0, i) + s.substring(i+1, s.length)
                if (sub in visited) continue
                visited.add(sub)
                dq.addLast(sub)
            }
        }
        return res
    }
}

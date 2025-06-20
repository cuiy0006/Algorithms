class Solution {
    fun partition(s: String): List<List<String>> {
        fun isPalindrome(i: Int, j: Int): Boolean {
            var i = i
            var j = j
            while (i < j) {
                if (s[i] != s[j]) return false
                i += 1
                j -= 1
            }
            return true
        }
        val res = mutableListOf<List<String>>()
        fun get_partitions(start: Int, curr: MutableList<String>) {
            if (start == s.length) {
                res.add(curr.toList())
                return
            }
            for (i in start..s.length-1) {
                if (!isPalindrome(start, i)) continue
                val sub = s.substring(start, i+1)
                curr.add(sub)
                get_partitions(i+1, curr)
                curr.removeLast()
            }
        }
        get_partitions(0, mutableListOf<String>())
        return res
    }
}

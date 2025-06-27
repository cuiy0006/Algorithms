class Solution {
    fun maxUniqueSplit(s: String): Int {
        var res = 0
        fun splitMax(idx: Int, curr: MutableSet<String>) {
            if (idx == s.length) {
                res = max(res, curr.size)
                return
            }
            for (i in idx..s.length-1) {
                val sub = s.substring(idx, i+1)
                if (sub in curr) continue
                curr.add(sub)
                splitMax(i+1, curr)
                curr.remove(sub)
            }
        }
        splitMax(0, mutableSetOf<String>())
        return res
    }
}

class Solution {
    private val cache = mutableMapOf(0 to 0, 1 to 1)

    fun fib(n: Int): Int {
        if (cache.containsKey(n)) return cache[n]!!

        val ret = fib(n-1) + fib(n-2)
        cache[n] = ret

        return ret
    }
}

class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var i = 0
        var j = matrix[0].size - 1

        while (i < matrix.size && j >= 0) {
            if (matrix[i][j] == target) return true
            if (matrix[i][j] < target) {
                i++
            } else {
                j--
            }
        }
        return false
    }
}

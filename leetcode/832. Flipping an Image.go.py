func flipAndInvertImage(A [][]int) [][]int {
    dic := map[int] int{1:0, 0:1}
    for i := range A{
        m := 0
        n := len(A) - 1
        for m < n{
            A[i][m], A[i][n] = dic[A[i][n]], dic[A[i][m]]
            m++
            n--
        }
        if m == n{
            A[i][m] = dic[A[i][m]]
        }
    }
    return A
}

func sortArrayByParity(A []int) []int {
    i := 0
    j := len(A) - 1
    for i < j{
        for i < j {
            if A[i] % 2 == 1{
                break
            }
            i++
        }
        
        for i < j{
            if A[j] % 2 == 0{
                break
            }
            j--
        }
        A[j], A[i] = A[i], A[j]
        
    }
    return A
}

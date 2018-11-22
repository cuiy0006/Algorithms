func rotateString(A string, B string) bool {
    i := 0
    for i <= len(A) {
        if A[i:] + A[:i] == B {
            return true
        }
        i++
    }
    return false
}

func hammingDistance(x int, y int) int {
    cnt := 0
    z := x ^ y
    for z != 0{
        cnt += z & 1
        z = z >> 1
    }
    return cnt
}

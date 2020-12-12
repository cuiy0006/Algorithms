func minMoves(nums []int) int {
    min := nums[0]
    for _, num := range nums{
        if num < min{
            min = num
        }
    }
    
    res := 0
    for _, num := range nums{
        res += num - min
    }
    return res
}

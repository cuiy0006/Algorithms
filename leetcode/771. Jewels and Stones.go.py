func numJewelsInStones(J string, S string) int {
    dic := make(map[rune] bool)
    for _, c := range J{
        dic[c] = true
    }
    
    cnt := 0
    for _, c := range(S){
        _, ok := dic[c]
        if ok {
            cnt++
        }
    }
    return cnt
}

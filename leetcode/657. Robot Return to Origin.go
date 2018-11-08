func judgeCircle(moves string) bool {
    left := 0
    up := 0
    for _, c := range moves{
        switch c{
            case 'U':
                up++
            case 'D':
                up--
            case 'L':
                left++
            case 'R':
                left--
        }
    }
    return left == 0 && up == 0
}

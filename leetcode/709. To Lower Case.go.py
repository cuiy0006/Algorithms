import "strings"

func toLowerCase(str string) string {
    arr := []rune(str)
    for i, c := range(arr){
        if rune(c) - rune('a') < 0 && rune(c) - rune('A') >= 0 && rune(c) - rune('A') < 26{
            arr[i] = rune('a') + rune(c) - rune('A')
        }
    }
    return string(arr)
}

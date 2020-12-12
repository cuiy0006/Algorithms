import "strings"
func uniqueMorseRepresentations(words []string) int {
    dic := make(map[rune] string)
    lst := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    for i, str := range lst{
        dic['a' + rune(i)] = str
    }
    
    word_dic := make(map[string] bool)
    var sb strings.Builder
    for _, word := range words{
        for _, c := range word{
            sb.WriteString(dic[c])
        }
        str := sb.String()
        word_dic[str] = true
        sb.Reset()
    }
    return len(word_dic)
}

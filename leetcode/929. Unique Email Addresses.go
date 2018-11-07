import "strings"

func numUniqueEmails(emails []string) int {
    dic := make(map[string] bool)
    for _, email := range emails{
        emailParts := strings.Split(email, "@")
        localName := emailParts[0]
        localName = strings.Split(email, "+")[0]
        localName = strings.Replace(localName, ".", "", -1)
        dic[localName + emailParts[1]] = true
    }
    return len(dic)
}

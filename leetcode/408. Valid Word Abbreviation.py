class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                k = i
                while k < len(abbr) and abbr[k].isdigit():
                    k += 1
                num = int(abbr[i:k])
                for _ in range(num):
                    j += 1
                    if j > len(word):
                        return False
                i = k
            else:
                if word[j] != abbr[i]:
                    return False
                i += 1
                j += 1

        return i == len(abbr) and j == len(word)
                
                
                

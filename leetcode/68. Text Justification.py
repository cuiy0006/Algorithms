class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        l = len(words[0])
        j = 1
        while j < len(words):
            n = j-i
            if l+len(words[j])+n > maxWidth:
                spaces = maxWidth - l
                if n != 1:
                    a = spaces % (n-1)
                    b = spaces // (n-1)
                    line = []
                    for k in range(i, j):
                        line.append(words[k])
                        if k != j-1:
                            if a > 0:
                                line.append(' '*(b+1))
                                a -= 1
                            else:
                                line.append(' '*b)
                else:
                    line = words[i] + ' '*(maxWidth-len(words[i]))
                res.append(''.join(line))
                l = len(words[j])
                i = j
            else:
                l += len(words[j])
            j += 1
        line = ' '.join(words[i:j+1])
        line += (maxWidth - len(line)) * ' '
        res.append(line)
        return res




class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j = i
            l = 0
            while j < len(words):
                l += len(words[j])
                if l > maxWidth:
                    break
                l += 1
                j += 1
                
            line = ''
            if j == len(words):
                line += ' '.join(words[i:])
                line += ' ' * (maxWidth - len(line))
            else:
                cnt = j - i
                if cnt == 1:
                    line = words[i]
                    line += ' ' * (maxWidth - len(line))
                else:
                    len_words = sum([len(words[idx]) for idx in range(i, j)])
                    num_space = (maxWidth - len_words) // (cnt - 1)
                    extra_space = (maxWidth - len_words) % (cnt - 1)

                    line = ''
                    for idx in range(i, j - 1):
                        line += words[idx] + ' ' * num_space
                        if extra_space != 0:
                            line += ' '
                            extra_space -= 1
                    line += words[j - 1]
                    
            res.append(line)
            i = j
        
        return res

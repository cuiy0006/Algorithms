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

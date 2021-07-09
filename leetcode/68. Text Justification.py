class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = [words[0]]
        currlen = len(words[0])
        
        for i in range(1, len(words)):
            word = words[i]
            if currlen + 1 + len(word) > maxWidth:
                lines.append(line)
                line = [word]
                currlen = len(word)
            else:
                line.append(word)
                currlen += 1 + len(word)
        
        if len(line) != 0:
            lines.append(line)
        
        res = []
        
        for i in range(len(lines)):
            line = lines[i]
            if i != len(lines) - 1:
                if len(line) == 1:
                    text = line[0] + ' ' * (maxWidth - len(line[0]))
                else:
                    length = 0
                    for word in line:
                        length += len(word)
                    
                    num_space = (maxWidth - length) // (len(line) - 1)
                    extra_space = (maxWidth - length) % (len(line) - 1)
                    text = line[0]
                    for j in range(1, len(line)):
                        word = line[j]
                        if extra_space != 0:
                            text += ' ' * (num_space + 1) + word
                            extra_space -= 1
                        else:
                            text += ' ' * num_space + word
            else:
                text = ' '.join(line)
                text += ' ' * (maxWidth - len(text))
            res.append(text)
        return res

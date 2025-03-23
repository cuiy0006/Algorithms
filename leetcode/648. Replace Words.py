class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Node()
        for word in dictionary:
            p = root
            for c in word:
                if c not in p.children:
                    p.children[c] = Node()
                p = p.children[c]
            p.word = word
        
        words = sentence.split(' ')
        res = []
        for word in words:
            p = root
            for c in word:
                if c not in p.children:
                    break
                p = p.children[c]
                if p.word is not None:
                    break
            if p.word is not None:
                res.append(p.word)
            else:
                res.append(word)
        return ' '.join(res)

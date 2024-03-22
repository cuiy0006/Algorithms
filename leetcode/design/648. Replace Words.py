class Node:
    def __init__(self):
        self.children = {}
        self.root = None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ancestor = Node()
        for root in dictionary:
            node = ancestor
            for c in root:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.root = root

        words = sentence.split(' ')
        for i, word in enumerate(words):
            node = ancestor
            for c in word:
                if c not in node.children:
                    break
                node = node.children[c]
                if node.root is not None:
                    words[i] = node.root
                    break
        return ' '.join(words)

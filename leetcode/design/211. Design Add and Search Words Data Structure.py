class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            if i == len(word)-1:
                node.is_end = True
            

    def search(self, word: str) -> bool:
        def search_from(idx, node):
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in node.children.values():
                        if search_from(i+1, child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]

            return node.is_end
        
        return search_from(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
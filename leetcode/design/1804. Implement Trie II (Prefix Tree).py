class Node:
    def __init__(self):
        self.children = {}
        self.word_end = 0
        self.word_pass = 0


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.word_pass += 1
        node.word_end += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.word_end
        

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.word_pass


    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                return
            node = node.children[c]
            node.word_pass -= 1
        node.word_end -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
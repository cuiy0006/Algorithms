class Trie:
    def __init__(self):
        self.word = None
        self.children = {}

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        root = Trie()
        for word in words:
            if word == '':
                continue
            node = root
            for i, c in enumerate(word):
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.word = word
        
        def helper(word, index, node):
            if index == len(word):
                return node.word != None and node.word != word
            c = word[index]
            if c not in node.children:
                return False
            if node.children[c].word != None and helper(word, index+1, root):
                return True
            return helper(word, index+1, node.children[c])
        
        res = []
        for word in words:
            if helper(word, 0, root):
                res.append(word)
        return res

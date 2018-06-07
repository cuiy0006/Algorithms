class Trie:
    def __init__(self):
        self.word = None
        self.children = {}
        

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        words = set(words)
        root = Trie()
        for word in words:
            node = root
            for i, c in enumerate(word):
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.word = word
        
        res = []
        def helper(row, col, node):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            if board[row][col] == '#':
                return
            c = board[row][col]
            if c not in node.children:
                return
            node = node.children[c]
            if node.word is not None:
                res.append(node.word)
                node.word = None
            
            board[row][col] = '#'
            helper(row + 1, col, node)
            helper(row - 1, col, node)
            helper(row, col + 1, node)
            helper(row, col - 1, node)
            board[row][col] = c
        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(i, j, root)
        return res          

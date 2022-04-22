class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word = None
        self.cnt = 0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for word in words:
            node = root
            for c in word:
                idx = ord(c)-ord('a')
                if node.children[idx] is None:
                    node.children[idx] = Node()
                node = node.children[idx]
                node.cnt += 1
            node.word = word
        
        res = set()
        def find_word(i, j, node):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            
            c = board[i][j]
            if c is None:
                return

            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return
            node = node.children[idx]
            if node.cnt == 0:
                return
            
            if node.word is not None:
                res.add(node.word)
                tmp = root
                for c in node.word:
                    idx = ord(c)-ord('a')
                    tmp = tmp.children[idx]
                    tmp.cnt -= 1
                node.word = None
            
            board[i][j] = None
            for x0, y0 in directions:
                find_word(i+x0, j+y0, node)
            board[i][j] = c
            
        for i in range(m):
            for j in range(n):
                find_word(i, j, root)

        return list(res)

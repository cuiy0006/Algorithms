class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        D = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def helper(index, i, j):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if word[index] != board[i][j]:
                return False
            board[i][j] = '#'
            for x0, y0 in D:
                if helper(index+1, i+x0, j+y0):
                    return True
            board[i][j] = word[index]
            return False
        
        for i in range(m):
            for j in range(n):
                if helper(0, i, j):
                    return True
        return False

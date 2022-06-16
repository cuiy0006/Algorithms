"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True, None, None, None, None)
        
        sub_n = n // 2
        topleft = [[0 for _ in range(sub_n)] for _ in range(sub_n)]
        topright = [[0 for _ in range(sub_n)] for _ in range(sub_n)]
        bottomleft = [[0 for _ in range(sub_n)] for _ in range(sub_n)]
        bottomright = [[0 for _ in range(sub_n)] for _ in range(sub_n)]

        total = 0
        for i in range(sub_n):
            for j in range(sub_n):
                topleft[i][j] = grid[i][j]
                total += grid[i][j]
        
        for i in range(sub_n):
            for j in range(sub_n, n):
                topright[i][j-sub_n] = grid[i][j]
                total += grid[i][j]
        
        for i in range(sub_n, n):
            for j in range(sub_n):
                bottomleft[i-sub_n][j] = grid[i][j]
                total += grid[i][j]
        
        for i in range(sub_n, n):
            for j in range(sub_n, n):
                bottomright[i-sub_n][j-sub_n] = grid[i][j]
                total += grid[i][j]
                
        if total == 0:
            return Node(0, True, None, None, None, None)
        if total == n * n:
            return Node(1, True, None, None, None, None)
        
        topleft_node = self.construct(topleft)
        topright_node = self.construct(topright)
        bottomleft_node = self.construct(bottomleft)
        bottomright_node = self.construct(bottomright)
        
        if topleft_node.val == topright_node.val and \
            topleft_node.val == bottomleft_node.val and \
            topleft_node.val == bottomright_node.val:
            return Node(topleft_node.val, False, topleft_node, topright_node, bottomleft_node, bottomright_node)
        else:
            return Node(0, False, topleft_node, topright_node, bottomleft_node, bottomright_node)

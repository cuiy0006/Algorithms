"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        root = node
        visited = {root: Node(root.val, [])}
        q = deque([root])

        while len(q) != 0:
            node = q.popleft()
            clone = visited[node]
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                clone.neighbors.append(visited[neighbor])

        return visited[root]


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        root = node
        visited = {root: Node(root.val, [])}
        
        def dfs(node, clone):
            if node is None:
                return
            
            for neighbor in node.neighbors:
                is_visited = neighbor in visited
                if not is_visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    dfs(neighbor, visited[neighbor])
                clone.neighbors.append(visited[neighbor])
        
        dfs(root, visited[root])
        return visited[root]


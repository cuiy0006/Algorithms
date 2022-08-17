"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        q = deque([node])
        cloned_node = Node(node.val)
        dic = {node: cloned_node}
        
        while len(q) != 0:
            node = q.popleft()
            cloned = dic[node]
            
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                cloned.neighbors.append(dic[neighbor])

        return cloned_node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def helper(node, parent):
            if node is None:
                return
            if parent is not None:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            helper(node.left, node)
            helper(node.right, node)
        
        helper(root, None)
        q = deque([target.val])
        seen = set()
        res = []

        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node in seen:
                    continue
                seen.add(node)
                if k == 0:
                    res.append(node)
                else:
                    for child in graph[node]:
                        q.append(child)
            k -= 1
        return res





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def preorder(node, parent):
            if node is None:
                return
            
            node.parent = parent
            preorder(node.left, node)
            preorder(node.right, node)
        
        preorder(root, None)
        res = []
        
        def find_nodes(node, distance, visited):
            if node is None or node in visited:
                return
            
            visited.add(node)
            if distance == k:
                res.append(node.val)
                return
            
            find_nodes(node.left, distance + 1, visited)
            find_nodes(node.right, distance + 1, visited)
            find_nodes(node.parent, distance + 1, visited)
            
        find_nodes(target, 0, set())
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def helper(node, distance):
            if node is None:
                return
            if distance == 0:
                res.append(node.val)
                return
            helper(node.left, distance-1)
            helper(node.right, distance-1)
        
        def traverse(node):
            if node is None:
                return None
            
            if node == target:
                helper(node, k)
                return 1
            
            left = traverse(node.left)
            right = traverse(node.right)
            if left is not None:
                if left == k:
                    res.append(node.val)
                elif left < k:
                    helper(node.right, k-left-1)
                return left+1
            if right is not None:
                if right == k:
                    res.append(node.val)
                elif right < k:
                    helper(node.left, k-right-1)
                return right+1
            return None
        
        traverse(root)
        return res



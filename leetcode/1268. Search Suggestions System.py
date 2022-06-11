class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.words = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node()
        
        for product in products:
            node = root
            for c in product:
                idx = ord(c) - ord('a')
                if node.children[idx] is None:
                    next_node = Node()
                else:
                    next_node = node.children[idx]

                node.children[idx] = next_node
                next_node.words.append(product)
                node = next_node
        
        res = []
        node = root
        for i, c in enumerate(searchWord):
            idx = ord(c)-ord('a')
            node = node.children[idx]
            if node is None:
                for _ in range(len(searchWord)-i):
                    res.append([])
                break
            node.words.sort()
            res.append(node.words[:3])
        
        return res
        
        

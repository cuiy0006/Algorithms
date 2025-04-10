class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            target = searchWord[:i+1]
            l = 0
            r = len(products)
            while l < r:
                mid = (l+r)//2
                if products[mid] < target:
                    l = mid+1
                else:
                    r = mid
            tmp = []
            while l < len(products) and len(tmp) < 3:
                word = products[l]
                if len(word) < len(target) or word[:len(target)] != target:
                    break
                tmp.append(word)
                l += 1
            res.append(tmp)
        return res




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
        
        

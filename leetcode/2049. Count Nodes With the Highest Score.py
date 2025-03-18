class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = defaultdict(list)
        root = None
        for child, parent in enumerate(parents):
            if parent == -1:
                root = child
            else:
                children[parent].append(child)
        
        product_cnt = {}
        def traverse(node):
            if len(children[node]) == 0:
                left = 0
                right = 0
            elif len(children[node]) == 1:
                left = traverse(children[node][0])
                right = 0
            else:
                left = traverse(children[node][0])
                right = traverse(children[node][1])

            product = 1
            rest = n-left-right-1
            if rest != 0:
                product *= rest
            if left != 0:
                product *= left
            if right != 0:
                product *= right
            if product not in product_cnt:
                product_cnt[product] = 0
            product_cnt[product] += 1
            return 1+left+right
        traverse(root)
 
        max_product = max(product_cnt.keys())
        return product_cnt[max_product]
            

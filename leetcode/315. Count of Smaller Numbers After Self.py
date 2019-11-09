class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.less_than_cnt = 0
        self.smaller = 0

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        root = Node(nums[-1])
        dic = {len(nums)-1: root}
        for i in range(len(nums)-2, -1, -1):
            num = nums[i]
            node = root
            less_than_cnt = 0
            while True:
                if num <= node.val:
                    node.smaller += 1
                    if node.left == None:
                        node.left = Node(num)
                        node.left.less_than_cnt = less_than_cnt
                        dic[i] = node.left
                        break
                    else:
                        node = node.left
                else:
                    less_than_cnt += node.smaller + 1
                    if node.right == None:
                        node.right = Node(num)
                        node.right.less_than_cnt = less_than_cnt
                        dic[i] = node.right
                        break
                    else:
                        node = node.right
        
        res = []
        for i in range(len(nums)):
            res.append(dic[i].less_than_cnt)
        return res

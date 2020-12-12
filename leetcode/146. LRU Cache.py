LAST, NEXT, KEY, VAL = 0, 1, 2, 3
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dic = {} #key -> node: [LAST, NEXT, KEY, VAL]
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dic, root, cap = self.dic, self.root, self.cap
        if key not in dic:
            return -1
        node =dic[key]
        node[NEXT][LAST], node[LAST][NEXT] = node[LAST], node[NEXT]
        root[LAST][NEXT], root[LAST], node[LAST], node[NEXT] = node, node, root[LAST], root
        return node[VAL]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        dic, root, cap = self.dic, self.root, self.cap
        if cap == 0:
            return
        if key in dic:
            self.get(key)
            dic[key][VAL] = value
            return
        if cap == len(dic):
            evict = root[NEXT]
            evict[NEXT][LAST], evict[LAST][NEXT] = evict[LAST], evict[NEXT]
            del dic[evict[KEY]]
        
        node = [None, None, key, value]
        root[LAST][NEXT], root[LAST], node[LAST], node[NEXT] = node, node, root[LAST], root
        dic[key] = node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





















class ListNode:
    def __init__(self, key, value, last, next):
        self.key = key
        self.value = value
        self.last = last
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {} #key-> node
        self.root = ListNode(None, None, None, None)
        self.root.next = self.root
        self.root.last = self.root
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dic, root = self.dic, self.root
        if key not in dic:
            return -1
        
        node = dic[key]
        node.last.next, node.next.last = node.next, node.last
        node.next, node.last = root.next, root
        root.next.last, root.next = node, node
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        dic, root, cap = self.dic, self.root, self.cap
        if cap == 0:
            return
        if key in dic:
            self.dic[key].value = value
            self.get(key)
            return
            
        if cap == len(dic):
            evict = root.last
            evict.last.next, evict.next.last = evict.next, evict.last
            del dic[evict.key]
            
        node = ListNode(key, value, root, root.next)
        root.next.last, root.next = node, node
        dic[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

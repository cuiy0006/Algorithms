class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {} #key -> [val, {}]

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        dic = self.dic
        for i, c in enumerate(key):
            if c not in dic:
                dic[c] = [0, {}]
            if i == len(key)-1:
                dic[c][0] = val
            dic = dic[c][1]

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        dic = self.dic
        sum_val = 0
        for c in prefix:
            if c not in dic:
                return 0
            sum_val = dic[c][0]
            dic = dic[c][1]
        
        def helper(dic):
            total = 0
            for val, new_dic in dic.values():
                total += helper(new_dic) + val
            return total
        
        return helper(dic) + sum_val
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

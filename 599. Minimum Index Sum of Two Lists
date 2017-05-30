class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i, name in enumerate(list1):
            dic[name] = i
        minval = sys.maxsize
        for i, name in enumerate(list2):
            if name in dic and dic[name] + i < minval:
                minval = dic[name] + i
                res = [name]
            elif name in dic and dic[name] + i == minval:
                res.append(name)
                
        return res

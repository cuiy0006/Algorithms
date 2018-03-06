from functools import reduce
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        lst = []
        tmp = num
        while tmp != 0:
            lst.append(tmp%10)
            tmp = tmp // 10
        lst = lst[::-1]
        sortedlst = sorted(lst, reverse=True)
        index = -1
        for i in range(len(lst)):
            if lst[i] != sortedlst[i]:
                index = i
                break
        if index == -1:
            return num
        for i in range(len(lst)-1, -1, -1):
            if lst[i] == sortedlst[index]:
                lst[index], lst[i] = lst[i], lst[index]
                break
        return reduce(lambda x,y: x*10 + y, lst)

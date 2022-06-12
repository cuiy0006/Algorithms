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

    
    
    
    
    
from heapq import heappush, heappop
from collections import deque

class Node:
    def __init__(self, digit):
        self.digit = digit
        self.q = deque()

    def __lt__(self, other):
        return self.digit > other.digit
    
        
class Solution:
    def maximumSwap(self, num: int) -> int:
        h = []
        lst = [int(digit) for digit in str(num)]
        dic = {}
        
        for i, digit in enumerate(lst):
            if digit not in dic:
                dic[digit] = Node(digit)
            dic[digit].q.append(i)

        for node in dic.values():
            heappush(h, node)
        
        for i, digit in enumerate(lst):
            if digit == h[0].digit:
                dic[digit].q.popleft()
                if len(dic[digit].q) == 0:
                    del dic[digit]
                    heappop(h)
            else:
                idx = h[0].q.pop()
                lst[i], lst[idx] = lst[idx], lst[i]
                break
        
        res = 0
        for digit in lst:
            res = res * 10 + digit
        return res
            
        

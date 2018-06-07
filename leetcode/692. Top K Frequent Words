from heapq import heappush
from heapq import heappop

class item:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt
    
    def __eq__(self, item):
        if self.word == item.word and self.cnt == item.cnt:
            return True
        else:
            return False
        
    def __lt__(self, item):
        if self.cnt < item.cnt or (self.cnt == item.cnt and self.word > item.word):
            return True
        else:
            return False

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        h = [] # item
        dic = {} # word -> freq
        for word in words:
            if word not in dic:
                dic[word] = 0
            dic[word] += 1
            
        for word, freq in dic.items():
            i = item(word, freq)
            heappush(h, i)
            if len(h) > k:
                heappop(h)
        res = []
        while len(h) != 0:
            res.append(heappop(h).word)
        res.reverse()
        return res
        
        
        
        
        
 class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 0
            dic[word] += 1
        
        lst = []
        for word, freq in dic.items():
            lst.append((-freq, word))
        lst.sort()
        lst = lst[:k]
        res = [word for _, word in lst]
        return res

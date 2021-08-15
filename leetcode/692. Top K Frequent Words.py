from heapq import heappush, heappop

class Node:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq > other.freq:
            return False
        elif self.freq < other.freq:
            return True
        else:
            return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        word_to_freq = {}
        for word in words:
            if word not in word_to_freq:
                word_to_freq[word] = 0
            word_to_freq[word] += 1
        
        for word, freq in word_to_freq.items():
            heappush(heap, Node(freq, word))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        while len(heap) != 0:
            res.append(heappop(heap))
            
        res.reverse()
        
        return [node.word for node in res]
        
        
        
        
        
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

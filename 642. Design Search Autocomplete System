from heapq import heappush
from heapq import heappop
class item:
    def __init__(self, freq, sentence):
        self.freq = freq
        self.sentence = sentence
        
    def __eq__(self, other):
        return self.freq == other.freq and self.sentence == other.sentence
    
    def __lt__(self, other):
        if self.freq < other.freq or (self.freq == other.freq and self.sentence > other.sentence):
            return True
        else:
            return False

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.dic = {} #prefix -> [sentence]
        self.freq_dic = {} # sentence -> freq
        self.curr = ''
        for j, sentence in enumerate(sentences):
            if sentence not in self.freq_dic:
                self.freq_dic[sentence] = 0
                for i in range(1, len(sentence)+1):
                    prefix = sentence[:i]
                    if prefix not in self.dic:
                        self.dic[prefix] = []
                    self.dic[prefix].append(sentence)
            self.freq_dic[sentence] += times[j]

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            if self.curr not in self.freq_dic:
                self.freq_dic[self.curr] = 0
                for i in range(1, len(self.curr)+1):
                    prefix = self.curr[:i]
                    if prefix not in self.dic:
                        self.dic[prefix] = []
                    self.dic[prefix].append(self.curr)
                
            self.freq_dic[self.curr] += 1
            self.curr = ''
            return []
        
        self.curr += c
        if self.curr not in self.dic:
            return []
        sentences = self.dic[self.curr]
        h = []
        for sentence in sentences:
            freq = self.freq_dic[sentence]
            i = item(freq, sentence)
            heappush(h, i)
            if len(h) > 3:
                heappop(h)
        res = []
        while len(h) != 0:
            res.append(heappop(h).sentence)
        res.reverse()
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

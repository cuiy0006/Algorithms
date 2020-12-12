class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix_dic = {}
        self.suffix_dic = {}
        for weight, word in enumerate(words):
            for i in range(min(len(word)+1, 11)):
                prefix = word[:i]
                suffix = word[len(word)-i:]
                if prefix not in self.prefix_dic:
                    self.prefix_dic[prefix] = []
                if suffix not in self.suffix_dic:
                    self.suffix_dic[suffix] = []
                self.prefix_dic[prefix].append(weight)
                self.suffix_dic[suffix].append(weight)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if prefix not in self.prefix_dic:
            return -1
        if suffix not in self.suffix_dic:
            return -1
        
        prefix_lst = self.prefix_dic[prefix]
        suffix_lst = self.suffix_dic[suffix]
        i = len(prefix_lst) -1
        j = len(suffix_lst) -1
        
        while i >= 0 and j >=0:
            if prefix_lst[i] < suffix_lst[j]:
                j-=1
            elif prefix_lst[i] > suffix_lst[j]:
                i-=1
            else:
                return prefix_lst[i]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

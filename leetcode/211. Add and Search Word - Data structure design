class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        dic = self.dic
        for i, c in enumerate(word):
            if c not in dic:
                dic[c] = [{}, False]
            if i == len(word) - 1:
                dic[c][1] = True
            dic = dic[c][0]
        
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(dic, word):
            for i, c in enumerate(word):
                if c == '.':
                    if i == len(word) - 1:
                        for _, (subdic, isEnd) in dic.items():
                            if isEnd:
                                return True
                        return False
                    subword = word[i+1:]
                    for _, (subdic, isEnd) in dic.items():
                        if helper(subdic, subword):
                            return True
                    return False
                if c not in dic:
                    return False
                if i == len(word) - 1:
                    return dic[c][1]
                dic = dic[c][0]
        return helper(self.dic, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

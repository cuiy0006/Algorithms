class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {} #key->set(index1...indexn)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        dic = self.dic
        for word in dict:
            for i, c in enumerate(word):
                new = word[:i] + word[i+1:]
                if new not in dic:
                    dic[new] = set()
                dic[new].add((i,c))

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        dic = self.dic
        for i, c in enumerate(word):
            new = word[:i] + word[i+1:]
            if new in dic and any(index==i and char!=c for index, char in dic[new]):
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = trieNode()
        for s in dict:
            node = root
            for i, c in enumerate(s):
                if node.lst[ord(c) - ord('a')] == None:
                    node.lst[ord(c) - ord('a')] = trieNode()
                node = node.lst[ord(c) - ord('a')]
            node.isWord = True
        
        words = sentence.split(' ')
        for i, word in enumerate(words):
            node = root
            for j, c in enumerate(word):
                if node.lst[ord(c) - ord('a')] == None:
                    break
                else:
                    node = node.lst[ord(c) - ord('a')]
                    if node.isWord:
                        words[i] = word[:j+1]
                        break
        
        return ' '.join(words)
        
        
class trieNode(object):
    def __init__(self):
        self.isWord = False
        self.lst = [None for i in range(26)]

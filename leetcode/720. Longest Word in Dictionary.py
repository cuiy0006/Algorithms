class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key=lambda word: (len(word), word))
        hashset = set()
        maxlen = 0
        res = None
        for word in words:
            if len(word) == 1:
                hashset.add(word)
                if len(word) > maxlen:
                    res = word
                    maxlen = len(word)
            else:
                if word[:-1] not in hashset:
                    continue
                else:
                    hashset.add(word)
                    if len(word) > maxlen:
                        res = word
                        maxlen = len(word)
        return res

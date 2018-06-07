class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        dic = {} #prefix -> []
        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                if prefix not in dic:
                    dic[prefix] = []
                dic[prefix].append(word)
        
        res = []
        def helper(index, curr):
            if index == len(words[0]):
                res.append(curr[:])
                return
            prefix = ''
            for i in range(index):
                prefix += curr[i][index]
            if prefix not in dic:
                return
            for word in dic[prefix]:
                curr.append(word)
                helper(index+1, curr)
                curr.pop()
        helper(0, [])
        return res

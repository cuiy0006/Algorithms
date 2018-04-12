class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {} # tuple (0)*26 -> [word]
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            tp = tuple(arr)
            if tp not in dic:
                dic[tp] = []
            dic[tp].append(s)
        return [lst for lst in dic.values()]

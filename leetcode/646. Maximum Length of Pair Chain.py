class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[1])
        curr = pairs[0]
        cnt = 1
        for pair in pairs:
            if pair[0] > curr[1]:
                curr = pair
                cnt += 1
        return cnt

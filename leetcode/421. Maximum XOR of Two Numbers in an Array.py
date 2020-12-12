class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = [None, None] #0, 1
        for num in nums:
            tmp = trie
            for i in range(31, -1, -1):
                curr_bit = (num >> i) & 1
                if tmp[curr_bit] is None:
                    tmp[curr_bit] = [None, None]
                tmp = tmp[curr_bit]
        
        max_val = 0
        for num in nums:
            tmp = trie
            total = 0
            for i in range(31, -1, -1):
                curr_bit = (num >> i) & 1
                if tmp[curr_bit ^ 1] is not None:
                    total += (1 << i)
                    tmp = tmp[curr_bit ^ 1]
                else:
                    tmp = tmp[not curr_bit ^ 1]
            max_val = max(max_val, total)
        return max_val

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        lst = []
        i = 0
        while i < numRows:
            tmp = [1]
            for j, num in enumerate(lst):
                if j != len(lst) - 1:
                    tmp.append(num + lst[j+1])
                else:
                    tmp.append(1)
            res.append(tmp)
            lst = tmp
            i += 1
        return res

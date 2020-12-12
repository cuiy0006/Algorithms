class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst = [0] * (rowIndex + 1)
        lst[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, -1, -1):
                if j == 0 or j == i + 1:
                    lst[j] = 1
                else:
                    lst[j] = lst[j] + lst[j-1]
        return lst

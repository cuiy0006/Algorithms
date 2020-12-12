class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dic = {}
        for row in wall:
            for i in range(len(row)-1):
                if i != 0:
                    row[i] += row[i-1]
                if row[i] not in dic:
                    dic[row[i]] = 1
                else:
                    dic[row[i]] += 1
        height = len(wall)
        return height - max(dic.values())

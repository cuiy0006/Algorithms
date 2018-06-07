class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        curr = 1
        res =[]
        for i in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                if curr == n:
                    curr = curr // 10
                curr += 1
                while curr % 10 == 0:
                    curr = curr // 10
        return res

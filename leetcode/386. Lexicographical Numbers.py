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


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def traverse(curr):
            if len(res) == n:
                return
            if curr > n:
                return
            if curr != 0:
                res.append(curr)
            start = 0 if curr != 0 else 1
            for i in range(start, 10):
                traverse(curr*10+i)

        traverse(0)
        return res


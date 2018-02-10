class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(B):
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = [i]
        res = [-1 for i in range(len(A))]
        for i, num in enumerate(A):
            res[i] = dic[num][-1]
            dic[num].pop()
        return res

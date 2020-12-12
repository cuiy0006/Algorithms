class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        arr1 = a.split('+')
        a1 = int(arr1[0])
        a2 = int(arr1[1][:-1])
        arr2 = b.split('+')
        b1 = int(arr2[0])
        b2 = int(arr2[1][:-1])
        
        p1 = a1 * b1 - a2 * b2
        p2 = a1 * b2 + a2 * b1
        res = str(p1) + '+' + str(p2) + 'i'
        return res

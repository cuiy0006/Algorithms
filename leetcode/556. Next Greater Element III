class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = list(str(n))
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i-=1
        if i < 0:
            return -1
        j = len(arr) - 1
        while j >= i+1:
            if arr[j] > arr[i]:
                break
            j -= 1
        arr[i],arr[j] = arr[j],arr[i]
        res = arr[:i+1] + sorted(arr[i+1:])
        res = int(''.join(res))
        if res > 2**31 -1:
            return -1
        else:
            return res

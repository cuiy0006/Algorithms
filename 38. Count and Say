class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curr = '1'
        for i in range(1, n):
            this_c = None
            next_val = ''
            cnt = 0
            for j, c in enumerate(curr):
                if this_c != c:
                    if this_c != None:
                        next_val += str(cnt) + this_c 
                    this_c = c
                    cnt = 1
                else:
                    cnt += 1
            next_val += str(cnt) + this_c
            curr = next_val
        return curr

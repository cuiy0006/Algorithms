class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def helper(s):
            lst = []
            tmp = ''
            for i, c in enumerate(s):
                if c != '+' and c != '-':
                    tmp += c
                else:
                    if tmp != '':
                        lst.append(tmp)
                    tmp = c
                if i == len(s)-1:
                    lst.append(tmp)
            res = [0, 0]
            for item in lst:
                if item[-1] == 'x':
                    val = item[:-1]
                    if len(val) ==0 or val[0] == '+' and len(val)==1:
                        res[0] += 1
                    elif val[0] == '-' and len(val) ==1:
                        res[0] += -1
                    else:
                        res[0] += int(item[:-1])
                else:
                    res[1] += int(item)
            return tuple(res)
            
        left, right = equation.split('=')
        leftx, leftval = helper(left)
        rightx, rightval = helper(right)
        if leftx != rightx:
            return 'x='+str((rightval - leftval)//(leftx - rightx))
        else:
            if leftval == rightval:
                return 'Infinite solutions'
            else:
                return 'No solution'

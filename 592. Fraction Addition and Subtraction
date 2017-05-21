class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        lst = []
        j = 0
        for i in range(len(expression)):
            if expression[i] == '+' or expression[i] == '-':
                s = expression[j:i]
                if s != '':
                    lst.append(s)
                j = i
            if i == len(expression) - 1:
                s = expression[j:]
                if s != '':
                    lst.append(s)
    
        res = reduce(self.helper, lst)
        res_lst = res.split('/')
        x_num = int(res_lst[0])
        x_den = int(res_lst[1])
        for i in [2, 3, 5, 7]:
            while x_num //i*i == x_num and x_den//i*i == x_den:
                x_num = x_num//i
                x_den = x_den//i
        res = str(x_num) + '/' + str(x_den)
        return res
            
            
    def helper(self, x, y):
        x_lst = x.split('/')
        y_lst = y.split('/')
        x_num = int(x_lst[0])
        x_den = int(x_lst[1])
        y_num = int(y_lst[0])
        y_den = int(y_lst[1])
        
        if x_den != y_den:
            den = x_den*y_den
            num = y_den*x_num + x_den*y_num
        else:
            den = x_den
            num = x_num + y_num
        return str(num) + '/' + str(den)
            
        

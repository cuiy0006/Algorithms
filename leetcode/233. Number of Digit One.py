# n = 123 [x] 456
# for 4th digit, how many combinations?

# x = 0 
#        123 * (999 + 1)                    :   (0 ~ 122) * (0 ~ 999)
# x = 1
#        1 * (456 + 1）+ 123 * (999 + 1)    :   1 * (0 ~ 456) + (0 ~ 122) * (0 ~ 999)
# x > 1
#        (123 + 1) * (999 + 1)              :   (0 ~ 123) * (0 ~ 999)

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        res = 0
        
        for i in range(len(s)):
            left = s[:i]
            right = s[i+1:]
            curr = int(s[i])
            
            
            left_num = 0 if left == '' else int(left)
            right_num = 0 if right == '' else int(right)
            
            if curr > 1:
                res += (left_num+1) * (10 ** len(right))
            elif curr == 1:
                res += (right_num+1) + left_num * (10 ** len(right))
            else:
                res += left_num * (10 ** len(right))
            
        return res
            

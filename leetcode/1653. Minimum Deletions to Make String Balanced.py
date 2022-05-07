class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_b = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == 'b':
                j = i
                while j < len(s) and s[j] == 'b':
                    j += 1
                num_b += j - i
                i = j
            else:
                if num_b == 0:
                    i += 1
                else:
                    j = i
                    while j < len(s) and s[j] == 'a':
                        j += 1
                    num_a = j - i
                    if num_a >= num_b:
                        res += num_b
                        num_b = 0
                    else:
                        res += num_a
                        num_b -= num_a
                    i = j
        return res
                

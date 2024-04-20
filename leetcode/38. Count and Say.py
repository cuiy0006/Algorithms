class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'

        for _ in range(1, n):
            i = 0
            j = 0
            next_curr = ''
            while i < len(curr):
                j = i+1
                while j < len(curr) and curr[j] == curr[j-1]:
                    j += 1
                next_curr += str(j-i) + curr[i]
                i = j
            curr = next_curr
        return curr
        

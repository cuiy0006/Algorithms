class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def is_valid(part):
            if part == '':
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            if int(part) > 255:
                return False
            return True
        
        
        for i in range(0, 3):
            if i > len(s) - 1:
                break
            part1 = s[:i+1]
            if not is_valid(part1):
                break
            
            for j in range(i+1, i+4):
                if j > len(s) - 1:
                    break
                part2 = s[i+1:j+1]
                if not is_valid(part2):
                    break
                
                for m in range(j+1, j+4):
                    if m > len(s) - 1:
                        break
                    part3 = s[j+1:m+1]
                    if not is_valid(part3):
                        break

                    part4 = s[m+1:]
                    if not is_valid(part4):
                        continue
                    res.append('.'.join([part1, part2, part3, part4]))
        return res

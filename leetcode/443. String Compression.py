class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        
        while i < len(chars):
            cnt = 1
            c = chars[i]
            i += 1
            while i < len(chars) and chars[i] == chars[i-1]:
                i += 1
                cnt += 1
            
            chars[j] = c
            j += 1
            if cnt == 1:
                continue
            cnt = str(cnt)
            for digit in cnt:
                chars[j] = digit
                j += 1
            
        return j
            

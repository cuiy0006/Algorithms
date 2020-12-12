class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0
        curr = chars[0]
        cnt = 1
        i = 1
        j = 0
        while i < len(chars):
            if chars[i] != chars[i-1]:
                chars[j] = curr
                j += 1
                if cnt > 1:
                    str_cnt = str(cnt)
                    for c in str_cnt:
                        chars[j] = c
                        j += 1
                curr = chars[i]
                cnt = 1
            else:
                cnt += 1
            i += 1
        
        chars[j] = curr
        j += 1
        if cnt > 1:
            str_cnt = str(cnt)
            for c in str_cnt:
                chars[j] = c
                j += 1
        return j

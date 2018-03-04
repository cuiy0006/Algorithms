class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i, j, start, end = 0, 0, 0, 0
        minlen = sys.maxsize
        cnt = len(t)
        dic = {c:0 for c in s}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        while j < len(s):
            if dic[s[j]] > 0:
                cnt -= 1
            dic[s[j]] -= 1
            j += 1
            while cnt == 0:
                if j - i < minlen:
                    minlen = j - i
                    start = i
                    end = j
                if dic[s[i]] == 0:
                    cnt += 1
                dic[s[i]] += 1
                i += 1
        return s[start:end]

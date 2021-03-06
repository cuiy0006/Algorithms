#better
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        dic = [0 for i in range(26)]
        for c in p:
            dic[ord(c)-ord('a')] += 1
        left=right=0
        cnt = len(p)
        while right < len(s):
            if dic[ord(s[right])-ord('a')] > 0:
                cnt -= 1
            dic[ord(s[right])-ord('a')] -= 1
            if right - left == len(p):
                if dic[ord(s[left])-ord('a')] >= 0:
                    cnt += 1
                dic[ord(s[left])-ord('a')] += 1
                left += 1
            if cnt == 0:
                res.append(left)
            right += 1
        return res
        
        

#mine
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def isSame(pdic, dic):
            for k,v in pdic.items():
                if k not in dic or dic[k] != v:
                    return False
            return True
        
        if len(s) < len(p):
            return []
        res = []
        pdic = {}
        for c in p:
            if c in pdic:
                pdic[c] += 1
            else:
                pdic[c] = 1
        dic = {}
        for i in range(len(p)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        if isSame(pdic, dic):
            res.append(0)
                
        for i in range(len(p), len(s)):
            dic[s[i-len(p)]]-=1
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            if isSame(pdic, dic):
                res.append(i-len(p)+1)
        return res

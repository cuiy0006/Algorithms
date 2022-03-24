class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            if s[i] in s_to_t and t[i] in t_to_s:
                if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
                    return False
            elif s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            else:
                return False

        return True

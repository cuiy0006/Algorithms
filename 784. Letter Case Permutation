class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [S]
        for i,c in enumerate(S):
            if c.isalpha():
                for j in range(len(res)):
                    s = res[j]
                    if c.islower():
                        res.append(s[:i] + c.upper() + s[i+1:])
                    else:
                        res.append(s[:i] + c.lower() + s[i+1:])
        return res

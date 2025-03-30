class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        s = list(s)
        def dfs(idx):
            if idx == len(s):
                res.append(''.join(s))
                return
            i = idx
            while i < len(s):
                if s[i].isnumeric():
                    i += 1
                else:
                    break
            if i != len(s):
                s[i] = s[i].upper()
                dfs(i+1)
                s[i] = s[i].lower()
                dfs(i+1)
            else:
                dfs(i)
        
        dfs(0)
        return res



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

class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R_cnt = senate.count('R')
        D_cnt = senate.count('D')
        n = len(senate)
        X_cnt = 0
        lst = list(senate)
        a = 0
        b = 0
        while X_cnt + R_cnt != n and D_cnt + X_cnt != n:
            for i, c in enumerate(lst):
                if c == 'R':
                    if b == 0:
                        a += 1
                    else:
                        b -= 1
                        lst[i] = 'X'
                        R_cnt -= 1
                        X_cnt += 1
                if c == 'D':
                    if a == 0:
                        b += 1
                    else:
                        a -= 1
                        lst[i] = 'X'
                        D_cnt -= 1
                        X_cnt += 1
        if X_cnt + R_cnt == n:
            return 'Radiant'
        else:
            return 'Dire'

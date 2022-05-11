class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = []
        dic = defaultdict(int)
        dup = False
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
            dic[s[i]] += 1
            if dic[s[i]] > 1:
                dup = True
        
        if len(diff) == 0 and dup:
            return True
        
        if len(diff) != 2:
            return False
        
        if s[diff[0]] != goal[diff[1]] or s[diff[1]] != goal[diff[0]]:
            return False
        return True

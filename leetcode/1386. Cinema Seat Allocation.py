class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        
        dic = {}
        for [row, col] in reservedSeats:
            if row not in dic:
                dic[row] = set()
            dic[row].add(col)
            
        res += (n - len(dic)) * 2
        
        for _, cols in dic.items():
            p23 = p45 = p67 = p89 = False
            
            if 2 not in cols and 3 not in cols:
                p23 = True
            if 4 not in cols and 5 not in cols:
                p45 = True
            if 6 not in cols and 7 not in cols:
                p67 = True
            if 8 not in cols and 9 not in cols:
                p89 = True
            
            if p23 and p45 or p67 and p89:
                if p23 and p45:
                    res += 1
                if p67 and p89:
                    res += 1
            else:
                if p45 and p67:
                    res += 1
        
        return res

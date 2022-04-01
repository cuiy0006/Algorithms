class Solution:
    def isNumber(self, s: str) -> bool:
        if s == '':
            return False
        
        def is_integer(si: str) -> bool:
            if si == '':
                return False
            i = 0
            if si[0] == '+' or si[0] == '-':
                if len(si) == 1:
                    return False
                i = 1
            while i < len(si):
                if not si[i].isdigit():
                    return False
                i += 1
            return True
        
        
        def is_float(sf: str) -> bool:
            if sf == '' or sf == '+' or sf == '-' or sf == '+.' or sf == '-.' or sf == '.':
                return False
            i = 0
            if sf[0] == '+' or sf[0] == '-':
                i = 1
            dot = 1
            while i < len(sf):
                if sf[i] == '.':
                    if dot == 0:
                        return False
                    dot -= 1
                else:
                    if not sf[i].isdigit():
                        return False
                i += 1
            return True
        
        
        s = s.replace('E', 'e')
        parts = s.split('e')
        if len(parts) == 1:
            if not is_float(parts[0]):
                return False
        elif len(parts) == 2:
            if not is_float(parts[0]) or not is_integer(parts[1]):
                return False
        else:
            return False
        
        return True
        

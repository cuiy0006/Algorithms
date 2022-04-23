class Solution:
    def decodeString(self, s: str) -> str:
        def evaluate(s):
            i = 0
            while s[i].isdigit():
                i += 1
            
            num = int(s[:i])
            part = s[i+1:-1]
            return num * part
        
        stack = []
        curr = ''
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                stack.append(curr)
                j = i+1
                while s[j].isdigit():
                    j += 1
                curr = s[i:j]
                i = j
            elif s[i] == ']':
                curr += ']'
                curr = stack.pop() + evaluate(curr)
                i += 1
            else:
                curr += s[i]
                i += 1
                
        return curr

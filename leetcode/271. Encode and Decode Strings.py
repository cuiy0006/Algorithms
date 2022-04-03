class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        end_idxs = []
        idx = 0
        res = ''
        for s in strs:
            idx += len(s)
            end_idxs.append(str(idx))
            res += s
        
        end_idx_str = ','.join(end_idxs)
        res = '[' + end_idx_str + ']' + res
        
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 1
        while s[i] != ']':
            i += 1
        
        end_idx_str = s[1:i]
        
        end_idxs = end_idx_str.split(',')
        
        encoded_s = s[i+1:]
        
        res = []
        
        start_idx = 0
        for end_idx in end_idxs:
            end_idx = int(end_idx)
            res.append(encoded_s[start_idx:end_idx])
            start_idx = end_idx
            
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

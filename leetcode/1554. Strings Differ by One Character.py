class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            pattern_set = set()
            for word in dict:
                pattern = word[:i] + '.' + word[i+1:]
                if pattern in pattern_set:
                    return True
                else:
                    pattern_set.add(pattern)
        
        return False

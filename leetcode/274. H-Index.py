class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x:-x)
        
        for i, cit in enumerate(citations):
            cnt = i + 1
            if cit == cnt:
                return cit
            elif cit < cnt:
                return cnt-1
        
        return len(citations)



class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(key=lambda x:-x)
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        return i

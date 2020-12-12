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

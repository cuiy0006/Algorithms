class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper(acc, needs):
            if all(need == 0 for need in needs):
                return acc
            if any(need < 0 for need in needs):
                return sys.maxsize
            
            curr = 0
            for i, need in enumerate(needs):
                curr += need * price[i]
            curr += acc
            for spec in special:
                tmpacc = acc + spec[-1]
                tmpneed = [need-spec[i] for i,need in enumerate(needs)]
                curr = min(curr, helper(tmpacc, tmpneed))
            return curr
                
        return helper(0, needs)

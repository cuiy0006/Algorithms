class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(key=lambda x:-x)
        res = deque()
        for card in deck:
            if len(res) != 0:
                res.appendleft(res.pop())
            res.appendleft(card)
        return list(res)


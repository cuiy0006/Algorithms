class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        print(cards)
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.01
        
        def get_new_card(card1, card2):
            res = [card1*card2, card1+card2, card1-card2, card2-card1]
            if card2 != 0:
                res.append(card1/card2)
            if card1 != 0:
                res.append(card2/card1)
            return res
        
        for i in range(len(cards)):
            for j in range(i+1, len(cards)):
                new_cards = [cards[k] for k in range(len(cards)) if k != i and k != j]

                for new_card in get_new_card(cards[i], cards[j]):
                    new_cards.append(new_card)
                    if self.judgePoint24(new_cards):
                        return True
                    new_cards.pop()

        return False

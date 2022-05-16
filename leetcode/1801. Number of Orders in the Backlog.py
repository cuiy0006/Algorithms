from heapq import heappush, heappop

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_heap = []
        sell_heap = []

        for [price, amount, option] in orders:
            if option == 0: # buy
                while len(sell_heap) != 0:
                    sell_price, sell_amount = sell_heap[0]
                    if sell_price > price:
                        break
                    if sell_amount > amount:
                        sell_heap[0][1] -= amount
                        amount = 0
                        break
                    elif sell_amount == amount:
                        heappop(sell_heap)
                        amount = 0
                        break
                    else:
                        heappop(sell_heap)
                        amount -= sell_amount
                if amount > 0:
                    heappush(buy_heap, [-price, amount])
            else:
                while len(buy_heap) != 0:
                    buy_price, buy_amount = buy_heap[0]
                    buy_price = -buy_price
                    if buy_price < price:
                        break
                    if buy_amount > amount:
                        buy_heap[0][1] -= amount
                        amount = 0
                        break
                    elif buy_amount == amount:
                        heappop(buy_heap)
                        amount = 0
                        break
                    else:
                        heappop(buy_heap)
                        amount -= buy_amount
                if amount > 0:
                    heappush(sell_heap, [price, amount])

        res = 0
        k = 1000000007
        for _, num in buy_heap:
            res += num
            res %= k

        for _, num in sell_heap:
            res += num
            res %= k

        return res
    
    
    #[[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]

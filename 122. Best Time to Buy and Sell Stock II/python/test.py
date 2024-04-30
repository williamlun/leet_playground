from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell_pointer = 1
        while sell_pointer < len(prices):
            if prices[sell_pointer] > prices[sell_pointer - 1]:
                profit += prices[sell_pointer] - prices[sell_pointer - 1]
            sell_pointer += 1
        return profit


test1 = [7, 1, 5, 3, 6, 4]
test2 = [1, 2, 3, 4, 5]
test3 = [7, 6, 4, 3, 1]

print(Solution().maxProfit(test1))
print(Solution().maxProfit(test2))
print(Solution().maxProfit(test3))

from typing import List


class myAns:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            for j in range(i + 1, len(prices)):
                temp = prices[j] - prices[i]
                profit = temp if temp > profit else profit
        # profit = max(profit, prices[i] - prices[j])
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_pointer = 0
        sell_pointer = 1
        while sell_pointer < len(prices):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            else:
                profit = max(profit, prices[sell_pointer] - prices[buy_pointer])
            sell_pointer += 1
        return profit


test_1 = [7, 1, 5, 3, 6, 4]
test_2 = [7, 6, 4, 3, 1]


print(Solution().maxProfit(test_1))
print(Solution().maxProfit(test_2))

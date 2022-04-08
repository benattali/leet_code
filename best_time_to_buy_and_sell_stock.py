class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        highest = prices[0]
        profit = -1

        for price in prices[1:]:
            if price < lowest:
                lowest = price
                highest = price
            elif price > highest:
                highest = price
                if highest - lowest > profit:
                    profit = highest - lowest
            else:
                continue

        if profit < 0:
            return 0

        return profit




prices = [7,6,4,3,1]
test = Solution().maxProfit(prices)
print(test)

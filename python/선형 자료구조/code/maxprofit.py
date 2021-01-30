def maxProfit(prices):
    lowest = prices[0]
    profit = 0

    for price in prices:
        if price < lowest:
            lowest = price

        if profit < (price - lowest):
            profit = price - lowest

    return profit


if __name__ == "__main__":
    prices = [1, 4, 6, 12, 2, 7, 6, 3]
    print(maxProfit(prices))

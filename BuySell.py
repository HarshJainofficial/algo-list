def maxProfit(prices):
    maxProfit = 0
    minPrice = float('inf')

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice

    return maxProfit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print("Maximum Profit:", result)

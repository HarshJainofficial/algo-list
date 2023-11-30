# Best Time To Buy And Sell 
def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Demo data
demo_prices = [7, 1, 5, 3, 6, 4]

# Calculate the result
result = max_profit(demo_prices)

# Print the input and output
print(f"Demo data: {demo_prices}")
print(f"The maximum profit is: {result}")

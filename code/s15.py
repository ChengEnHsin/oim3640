prices = {'AAPL': 260.81, 'NVDA': 186.00, 'MSFT': 404.88, 'GOOG': 308.42}

# 1. Get the price of 'AAPL'
print(prices['AAPL'])

# 2. What happens if you do prices['TSLA']
# This would raise a KeyError because 'TSLA' is not in the dictionary
print(prices.get('TSLA'))  # safer way, returns None

# 3. Find the stock with the highest price
highest_stock = max(prices, key=prices.get)
print(highest_stock, prices[highest_stock])

# 4. Get a list of all stocks priced above $200
above_200 = [stock for stock, price in prices.items() if price > 200]
print(above_200)

# 5. If all prices go up 10%, update all values
for stock in prices:
    prices[stock] *= 1.10

print(prices)


def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

result = histogram('bookkeeper')
print(result['o'])
print(result.get('o', 0))
print(result.get('z', 0))



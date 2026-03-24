import yfinance as yf
stock = yf.Ticker("AAPL")
info = stock.info
print(info['shortName'])
print(info['currentPrice'])
print(info.keys())
print(len(info.keys()))
print(info['longName'])

print(info['longBusinessSummary'])

print(info['longBusinessSummary'].split())
#break it down into tokens, which are words and punctuation. spaces between words

print('iphone'in info['longBusinessSummary'].lower())
#case sensitive, should change to lower case or upper case to make it work

print(info['city'])
info['city'] = 'Wellesley'
#string can't use lowercase
#lists starts with square brackets, dictionaries start with curly braces
print(info['city'])
len(info)
#tells me how many attributes there are in the info dictionary

#what other keys are there in the info dictionary?
#list can be a collection of anything

tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']


print(sorted(prices)) #creates a new list of the keys in prices, sorted alphabetically
print(sorted(prices.values(), reverse=True)) #creates a new list of the values in prices, sorted from highest to lowest, decending order

print(tickers)

#get total value of all 3 stocks
print(sum(prices.values()))

tickers = ['AAPL', 'NVDA', 'MSFT', 'META', 'GOOG']
stocks = {} # {'NVDA' : [open, currentPrice, volume]}

for t in tickers:
    stocks[t] = [yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume']]
print(stocks)

#difference between tuples and lists is that tuples are immutable, meaning they cannot be changed after they are created, while lists are mutable and can be modified. 
#Tuples are defined using parentheses () and lists are defined using square brackets [].

stocks['AAPL'][1]=260
print(stocks)

info_list = {}
for name in ['open', 'currentPrice', 'volume']:
    info_list[name] = yf.Ticker(t).info[name]
    stocks[t]= info_list
    print(stocks)

#get familiar with mixed types of data structures, like dictionaries that contain lists, or dictionaries that contain other dictionaries.
#if a function returns multiple values, it is often returning a tuple, which is an ordered collection of values that can be of different types.
#unpacking a tuple means assigning its values to individual variables. For example, if a function returns a tuple like (a, b, c), you can unpack it like this: x, y, z = function().

#unhashable type error occurs when you try to use a mutable type, such as a list or a dictionary, as a key in a dictionary. This is because keys in a dictionary must be immutable, meaning they cannot be changed after they are created.
#To fix this error, can use a tuple instead of a list or a dictionary as the key, since tuples are immutable. For example, instead of using a list like [1, 2] as a key, you can use a tuple like (1, 2).
#tuples can replace lists in dictonaries as keys

#use sets when want to get unique values; sets are mutable, defined with curly braces, unordered and do not duplicate elements, and useful for union, intersection, and difference operations.
#set would be much faster if you want to check if an element is in a collection, because sets are implemented as hash tables, which allow for constant time complexity for membership tests, while lists have linear time complexity for membership tests.

#quiz will be which data structure to use for a given problem, and how to manipulate it and give examples of how to use it.


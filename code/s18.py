words = 'the cat sat on the mat'.split()
print(len(words))
print(len(set(words)))
#What does each print output?
#6
#Why are the two numbers different?
#5, removes redundant words, only counts unique words

def mystery(s):
    return len(set(s)) == len(s)

print(mystery('hello'))
print(mystery('world'))
#What does each print output?
#False, because there are 2 'l's
#What does mystery check for?
#It checks if all characters in the string are unique, meaning there are no duplicate characters. 
#If the length of the set of characters is equal to the length of the original string, then all characters are unique and the function returns True. Otherwise, it returns False.


#lambda functions are anonymous functions that can be defined in a single line of code.
#They are often used for short, simple functions that are not worth defining with a full function definition.
#usually only used once, and can be passed as arguments to other functions, such as sorted() or map().
freq = {'a': 3, 'b': 1, 'c': 2}
result = sorted(freq.items(), key=lambda x: x[1])
print(result)
#What does result look like?
#How would you get the item with the highest count?
#result is a list of tuples, sorted by the second element of each tuple (the count). The output would be: [('b', 1), ('c', 2), ('a', 3)]

try:
    age = int(input('Your age: '))
    print(f'You are {age} years old')
except ValueError:
    print('That is not a valid number!')
#Code in try runs normally
#If an error occurs, Python jumps to except
#Program keeps running instead of crashing

scores = {'Alice': 95, 'Bob': 87}

try:
    name = input('Student name: ')
    print(f'{name}: {scores[name]}')
except KeyError:
    print(f'{name} not found')
#Always catch specific exceptions, not bare except:.



a = input("enter an integer: ") # how to make sure input is integer
a = int(a)  # convert string input to integer
print(type(a))

# check odd or even

if a % 2 == 0:
    print("Even")
else:
    print("Odd")


product = 100 #in dollars
tax_rate = 0.0625 # 6.25%
tax = product * tax_rate
print(f'tax is ${tax}.')  # f strings

def calc_tax(price):
    """calculate tax on given price"""
    tax_rate = 0.0625 # 6.25%
    tax = price * tax_rate
  #  print(f'tax is ${tax}.')  # f strings
# if the function doesn't explicitly returnany value, it returns None
#calc_tax(100)
    return tax


#total_tax = calc_tax(computer_price)+ calc_tax(iphone_price)
#print(total_tax)

computer_price = float(input("enter computer price: "))
iphone_price = 1100
tax_computer = calc_tax(computer_price)
tax_iphone = calc_tax(iphone_price)


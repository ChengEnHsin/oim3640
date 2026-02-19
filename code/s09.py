def evaluation_score(score):
    if score >= 90:
        return "excellent work!"
    if score <= 60:
        return "passed"
    else:
        return "failed"


for i in range(5):
    print(i)


#while loop intro
i = 0
while i < 5:
    print(i)
    i+=1

n = 3
while n > 0:
    print(n)
    n -= 1
print("Go!")
# 3, 2, 1, Go!


#example from ai

password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access granted")

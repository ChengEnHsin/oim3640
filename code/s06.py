def draw_square(size):
    for i in range(size):
       # print("🧱"*size)
       for j in range(size):
            print("🧱", end="")
       print('Hello')

#   draw a triangle - could be in quiz

def draw_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("🧱", end="")
        print()

#another way
    for i in range(1, size + 1):
        print("🧱" * i)
draw_triangle(4)

#draw an inverse triangle
def draw_inverse_triangle(size):
    for i in range(size, 0, -1):
        print("🧱" * i)
draw_inverse_triangle(5)

#create a function that draws a pyramid

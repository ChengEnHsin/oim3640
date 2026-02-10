import turtle
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)  

def draw_spiral():
    draw_square(t, 20)
    t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_square(t)
    draw_square(t, 50)
    turtle.mainloop()

if __name__ == "__main__":
    main()
    
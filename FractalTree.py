import turtle
t = turtle.Turtle()
t.left(90)
t.speed(150)
def tree(j):
    if j<10:
        return
    else:
        t.forward(j)
        t.left(30)
        tree(3*j/4)
        t.right(60)
        tree(3*j/4)
        t.left(30)
        t.backward(j)
tree(100)
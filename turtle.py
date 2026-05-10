import turtle

def draw_square(size, color_name):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color_name)
    t.speed(2)
    
    for _ in range(4):        # Loop 4 times
        t.forward(size)
        t.left(90)
    
    turtle.done()

# Draw a blue square of size 100
draw_square(100, "blue")i
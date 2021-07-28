# imports
import turtle


# screen 
wn = turtle.Screen()
wn.title("PONG TEST")
wn.bgcolor("black")
wn.setup(width=500, height=320)
wn.tracer(0)

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape('arrow')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(0, 0)
paddle_a.shapesize(5, 1)


# Main game loop
while True:
    wn.update()

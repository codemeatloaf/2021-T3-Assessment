# imports
import turtle


# screen 
wn = turtle.Screen()
wn.title("PONG TEST")
wn.bgcolor("black")
wn.setup(width=500, height=320)
wn.tracer(0)


# Main game loop
while True:
    wn.update()

# Import modules
import turtle as trtl
import random, time
# Choose colors for each of the turtles
player1color = input("What color do you want player 1 to be?")
player2color = input("What color do you want player 2 to be?")
while player1color == player2color:
  print("!!!   Cannot have same player colors   !!!")
  player1color = input("What color do you want player 1 to be?")
  player2color = input("What color do you want player 2 to be?")
while player1color == "white" or player2color == "white":
  print("!!!   Color cannot be white, it blends with the map   !!!")
  player1color = input("What color do you want player 1 to be?")
  player2color = input("What color do you want player 2 to be?")

# Setup to move the turtles to the default positions.
turtles = []
score = 1
for x in range(2):
  turtles.append(trtl.Turtle())
turtles[0].penup()
turtles[0].shape("circle")
turtles[0].shapesize(2)
turtles[0].fillcolor(player1color)
turtles[1].penup()
turtles[1].shape("circle")
turtles[1].shapesize(2)
turtles[1].fillcolor(player2color)
turtles[0].goto(-100, -100)
turtles[1].goto(100, 100)

# Set up the text turtles
font_setup = ("Arial", 20, "normal")
turtle1keys = trtl.Turtle()
turtle1keys.pu()
turtle1keys.goto(-300, 200)
turtle1keys.pd()
turtle1keys.ht()
turtle1keys.write("Player 1: {color}".format(color=player1color),
                  font=font_setup)

turtle2keys = trtl.Turtle()
turtle2keys.pu()
turtle2keys.goto(150, 200)
turtle2keys.pd()
turtle2keys.ht()
turtle2keys.write("Player 2: {color}".format(color=player2color),
                  font=font_setup)

winTurtle = trtl.Turtle()
winTurtle.pu()
winTurtle.ht()

# Define all functions below
def resetTurtles(turtle1, turtle2):
  turtle1.goto(-100, -100)
  turtle2.goto(100, 100)



def checkCollision():
  global score
  if abs(turtles[0].xcor() - turtles[1].xcor() < 5
      and abs(turtles[0].ycor() - turtles[1].ycor()) < 5):
    resetTurtles(turtles[0], turtles[1])
    score += 1



  
def endGame():
  winTurtle.goto(-100, 0)
  winTurtle.write("Game over, score is {score}".format(score=score),
                  font=font_setup)
  resetTurtles(turtles[1], turtles[0])


def turtle1right():
  turtles[0].setheading(0)
  turtles[0].forward(5)
  checkCollision()


def turtle1left():
  turtles[0].setheading(180)
  turtles[0].forward(5)
  checkCollision()

def turtle1up():
  turtles[0].setheading(90)
  turtles[0].forward(5)
  checkCollision()

def turtle1down():
  turtles[0].setheading(270)
  turtles[0].forward(5)
  checkCollision()

def turtle2right():
  turtles[1].setheading(0)
  turtles[1].forward(5)
  checkCollision()

def turtle2left():
  turtles[1].setheading(180)
  turtles[1].forward(5)
  checkCollision()

def turtle2up():
  turtles[1].setheading(90)
  turtles[1].forward(5)
  checkCollision()

def turtle2down():
  turtles[1].setheading(270)
  turtles[1].forward(5)
  checkCollision()

# All events are stored here
wn = trtl.Screen()
wn.tracer(True)
wn.onkeypress(lambda: turtle1right(), "d")
wn.onkeypress(lambda: turtle1left(), "a")
wn.onkeypress(lambda: turtle1up(), "w")
wn.onkeypress(lambda: turtle1down(), "s")

wn.onkeypress(lambda: turtle2right(), "Right")
wn.onkeypress(lambda: turtle2left(), "Left")
wn.onkeypress(lambda: turtle2up(), "Up")
wn.onkeypress(lambda: turtle2down(), "Down")

wn.onkeypress(lambda: endGame(), "Escape")
wn.listen()
wn.update()
wn.mainloop()


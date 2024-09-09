#Import statements
import time
import turtle as trtl
import random as rand


#Functions
#TicTacToe Functions
def drawTicTacToe(trtl, size):
  for i in range(3):
    for k in range(3):
      for j in range(4):
        trtl.forward(size)
        trtl.lt(90)
      trtl.forward(size)
    trtl.penup()
    trtl.goto(0, trtl.ycor() + size)
    trtl.pendown()


def drawX(trtl, size):
  trtl.pu()
  tempXcoords = rand.choice(computerXcoords)
  tempYcoords = rand.choice(computerYcoords)
  if len(usedCoords) > 0:
    while (tempXcoords, tempYcoords) in usedCoords:
      tempXcoords = rand.choice(computerXcoords)
      tempYcoords = rand.choice(computerYcoords)
  trtl.goto(tempXcoords, tempYcoords)
  usedCoords.append((tempXcoords, tempYcoords))
  computerCoords.append((tempXcoords, tempYcoords))

  trtl.pd()
  trtl.setheading(-45)
  trtl.forward(size)
  trtl.back(size / 2)
  trtl.setheading(45)
  trtl.forward(size / 2)
  trtl.back(size)
  trtl.forward(size / 2)
  trtl.setheading(135)
  trtl.forward(size / 2)


def drawO(trtl, radius):
  global moves
  trtl.pu()
  #tempXcoords = tup(0)
  #tempYcoords = tup(1)
  #if len(usedCoordsComputer) > 0 or len(usedCoordsPlayer):
  #while (tempXcoords, tempYcoords) in usedCoordsComputer or (
  #tempXcoords, tempYcoords) in usedCoordsPlayer:
  #tempXcoords = random.choice(computerXcoords)
  #tempYcoords = random.choice(computerYcoords)
  trtl.goto(tempXcoords, tempYcoords)
  usedCoords.append((tempXcoords, tempYcoords))
  playerCoords.append((tempXcoords, tempYcoords))
  trtl.pd()
  trtl.circle(radius)
  moves += 1
  movesIndicator.clear()
  movesIndicator.write("Moves: {moves}".format(moves=moves), font=font_setup)


def checkForPlayerWin():
  if (25, 130) in playerCoords and (75, 130) in playerCoords and (
      125, 130) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 80) in playerCoords and (75, 80) in playerCoords and (
      125, 30) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 30) in playerCoords and (75, 30) in playerCoords and (
      125, 80) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 130) in playerCoords and (25, 80) in playerCoords and (
      25, 30) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (75, 130) in playerCoords and (75, 80) in playerCoords and (
      75, 30) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (125, 130) in playerCoords and (125, 30) in playerCoords and (
      125, 80) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 130) in playerCoords and (75, 80) in playerCoords and (
      125, 80) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 30) in playerCoords and (75, 80) in playerCoords and (
      125, 130) in playerCoords:
    print("Player wins")
    wn.clear()
    drawConnectBoard()


def checkForComputerWin():
  if (25, 130) in computerCoords and (75, 130) in computerCoords and (
      125, 130) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 80) in computerCoords and (75, 80) in computerCoords and (
      125, 30) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 30) in computerCoords and (75, 30) in computerCoords and (
      125, 80) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 130) in computerCoords and (25, 80) in computerCoords and (
      25, 30) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (75, 130) in computerCoords and (75, 80) in computerCoords and (
      75, 30) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (125, 130) in computerCoords and (125, 30) in computerCoords and (
      125, 80) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 130) in computerCoords and (75, 80) in computerCoords and (
      125, 80) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()
  elif (25, 30) in computerCoords and (75, 80) in computerCoords and (
      125, 130) in computerCoords:
    print("Computer wins")
    wn.clear()
    drawConnectBoard()


#Connect 4 Functions
#Drawing the connect 4 board
def drawConnectBoard():
  global openSpaceTrtlList
  global redSpaceList
  global yellowSpaceList
  global turn
  global currentColor
  openSpaceTrtlList = []
  redSpaceList = []
  yellowSpaceList = []
  currentColor = 'red'
  turn = 0
  wn.tracer(0)
  wn.bgcolor('royal blue')
  spotX = 65
  spotY = 65
  redSpaceList = []
  yellowSpaceList = []
  openSpaceTrtlList = []
  turn = 0
  #Placing a turtle at every space in the game
  for k in range(8):
    for i in range(8):
      i = trtl.Turtle()
      i.penup()
      i.goto(spotX - 290, spotY - 290)
      i.color('black')
      i.shape('circle')
      i.shapesize(3)
      i.pendown()
      i.stamp()
      i.onclick(clicked)
      openSpaceTrtlList.append(i)
      spotX += 65
    spotY += 65
    spotX = 65
  wn.tracer(1)


#If a turtle is clicked this sees which turtle is clicked and sees if the bot needs to make a move
def clicked(x, y):
  global redSpaceList
  global yellowSpaceList
  global currentColor
  global turn
  for i in openSpaceTrtlList:
    if (abs(x - i.xcor()) <= 30):
      i.color(currentColor)
      openSpaceTrtlList.remove(i)
      break
  if (currentColor == 'red'):
    turn += 1
    currentColor = 'yellow'
    redSpaceList.append(i)
    checkWins(redSpaceList)
    botMove()
  else:
    turn += 1
    currentColor = 'red'
    yellowSpaceList.append(i)
    checkWins(yellowSpaceList)


#The function for the bot making a move
def botMove():
  global redSpaceList
  global yellowSpaceList
  #If the player has not even had a chance to play anything that needs to be blocked, then the bot selects a random column to select
  if (turn < 5):
    clicked((rand.randint(-3, 4) * 65), 0)
    return
#Gaining data to see in what ways the user could be near a win and what the coordinates of the spaces in that particular position are
  vertMatch = checkVertWin(redSpaceList)
  horizMatch = checkHorizWin(redSpaceList)
  posDiagMatch = checkDiagPosWin(redSpaceList)
  negDiagMatch = checkDiagNegWin(redSpaceList)
  block = True
  #Checking if the player has three in a row vertically somewhere, if the player is near a win vertically, then the bot will block them
  if (vertMatch[0] == 2):
    for i in yellowSpaceList:
      if (i.ycor() == vertMatch[2] + 65 and i.xcor() == vertMatch[1]
          and vertMatch[2] + 65 > 230):
        block = False
    if (block == True):
      clicked(vertMatch[1], 0)
      return
  block = True
  block1 = True
  #Checking if the player has three in a row horizontally somewhere, if the player is near a win horizontally, then the bot will block them
  if (horizMatch[0] == 2):
    for i in yellowSpaceList:
      if (i.xcor() == horizMatch[2] + 65 and i.ycor() == horizMatch[3]
          and horizMatch[2] + 65 < 230):
        block = False
      elif (i.xcor() == horizMatch[1] - 65 and i.ycor() == horizMatch[3]
            and horizMatch[1] - 65 < -225):
        block1 = False
    if (block1 == True and block == True):
      leftORight = [horizMatch[1] - 65, horizMatch[2] + 65]
      clicked(rand.choice(leftORight), 0)
      return
    elif (block1 == True and block == False and horizMatch[1] - 65 > -250):
      clicked(horizMatch[1] - 65, 0)
      return
    elif (block1 == False and block == True):
      clicked(horizMatch[2] + 65, 0)
      return
  block = True
  block1 = True
  #Checking if the player has three in a row diagonally with a slope of 1 somewhere, if the player is near a win diagonally, then the bot will block them
  if (posDiagMatch[0] == 2):
    for i in yellowSpaceList:
      if (i.xcor() == posDiagMatch[3] + 65 and i.ycor() == posDiagMatch[4] + 65
          and posDiagMatch[3] + 65 < 230 and posDiagMatch[4] + 65 < 230):
        block = False
      elif (i.xcor() == posDiagMatch[1] - 65
            and i.ycor() == posDiagMatch[2] - 65
            and posDiagMatch[1] - 65 > -225 and posDiagMatch[2] - 65 > -225):
        block1 = False
    if (block1 == True and block == True):
      upODown = [posDiagMatch[1] - 65, posDiagMatch[3] + 65]
      clicked(rand.choice(upODown), 0)
      return
    elif (block1 == True and block == False):
      clicked(posDiagMatch[1] - 65, 0)
      return
    elif (block1 == False and block == True):
      clicked(posDiagMatch[3] + 65, 0)
      return
  block = True
  block1 = True
  #Checking if the player has three in a row diagonally with a slope of -1 somewhere, if the player is near a win diagonally, then the bot will block them
  if (negDiagMatch[0] == 2):
    for i in yellowSpaceList:
      if (i.xcor() == negDiagMatch[3] - 65 and i.ycor() == negDiagMatch[4] + 65
          and negDiagMatch[3] - 65 < -230 and negDiagMatch[4] + 65 < 230):
        block = False
      elif (i.xcor() == negDiagMatch[1] + 65
            and i.ycor() == negDiagMatch[2] - 65 and negDiagMatch[1] + 65 > 225
            and negDiagMatch[2] - 65 > -225):
        block1 = False
    if (block1 == True and block == True):
      upODown = [negDiagMatch[1] + 65, negDiagMatch[3] - 65]
      clicked(rand.choice(upODown), 0)
      return
    elif (block1 == True and block == False):
      clicked(negDiagMatch[1] + 65, 0)
      return
    elif (block1 == False and block == True):
      clicked(negDiagMatch[3] - 65, 0)
      return
#This ensures that if the player is not near winning, then the bot still plays but picks a random column
  clicked((rand.randint(-3, 4) * 65), 0)


#Checking if the player or the bot have won vertically by checking every space they have used and looking up three more spaces to see if those spaces are the same color
def checkVertWin(colorSpaceList):
  ultSpaceMatch = 0
  startSpace = 0
  secLastSpace = 0
  for i in colorSpaceList:
    spaceMatch = 0
    for k in colorSpaceList:
      if (k.xcor() == i.xcor() and k.ycor != i.ycor):
        if (abs(k.ycor() - i.ycor()) == 65 and spaceMatch == 0):
          spaceMatch += 1
        elif (abs(k.ycor() - i.ycor()) == 130 and spaceMatch == 1):
          spaceMatch += 1
          secLastSpace = k.ycor()
          ultSpaceMatch = spaceMatch
          startSpace = i.xcor()
        elif (abs(k.ycor() - i.ycor()) == 195 and spaceMatch == 2):
          spaceMatch += 1
      if (spaceMatch == 3):
        return True
  return [ultSpaceMatch, startSpace, secLastSpace]


#Checking if the player or the bot have won horizontally by checking every space they have used and looking right three more spaces to see if those spaces are the same color
def checkHorizWin(colorSpaceList):
  ultSpaceMatch = 0
  startSpaceX = 0
  startSpaceY = 0
  secLastSpace = 0
  for i in colorSpaceList:
    spaceMatch = 0
    for k in colorSpaceList:
      if (k.ycor() == i.ycor() and k.xcor != i.xcor):
        if (abs(k.xcor() - i.xcor()) == 65 and spaceMatch == 0):
          spaceMatch += 1
        elif (abs(k.xcor() - i.xcor()) == 130 and spaceMatch == 1):
          spaceMatch += 1
          secLastSpace = k.xcor()
          startSpaceX = i.xcor()
          startSpaceY = i.ycor()
          ultSpaceMatch = spaceMatch
        elif (abs(k.xcor() - i.xcor()) == 195 and spaceMatch == 2):
          spaceMatch += 1
      if (spaceMatch == 3):
        return True
  return [ultSpaceMatch, startSpaceX, secLastSpace, startSpaceY]


#Checking if the player or the bot have won diagonally by checking every space they have used and looking in a line with a slope of 1 for three more spaces
def checkDiagPosWin(colorSpaceList):
  ultSpaceMatch = 0
  startSpaceX = 0
  startSpaceY = 0
  secLastSpaceX = 0
  secLastSpaceY = 0
  for i in colorSpaceList:
    spaceMatch = 0
    for k in colorSpaceList:
      if (i.xcor() < k.xcor() and i.ycor() < k.ycor()):
        if (abs(i.xcor() - k.xcor()) == 65 and abs(i.ycor() - k.ycor()) == 65
            and spaceMatch == 0):
          spaceMatch += 1
        elif (abs(i.xcor() - k.xcor()) == 130
              and abs(i.ycor() - k.ycor()) == 130 and spaceMatch == 1):
          spaceMatch += 1
          secLastSpaceX = k.xcor()
          secLastSpaceY = k.ycor()
        elif (abs(i.xcor() - k.xcor()) == 195
              and abs(i.ycor() - k.ycor()) == 195 and spaceMatch == 2):
          spaceMatch += 1
        if (spaceMatch == 3):
          return True
    if (spaceMatch >= ultSpaceMatch):
      ultSpaceMatch = spaceMatch
      startSpaceX = i.xcor()
      startSpaceY = i.ycor()
  return [
      ultSpaceMatch, startSpaceX, startSpaceY, secLastSpaceX, secLastSpaceY
  ]


#Checking if the player or the bot have won diagonally by checking every space they have used and looking in a line with a slope of -1 for three more spaces
def checkDiagNegWin(colorSpaceList):
  ultSpaceMatch = 0
  startSpaceX = 0
  startSpaceY = 0
  secLastSpaceX = 0
  secLastSpaceY = 0
  for i in colorSpaceList:
    spaceMatch = 0
    for k in colorSpaceList:
      if (i.xcor() > k.xcor() and i.xcor() > k.xcor()):
        if (abs(i.xcor() - k.xcor()) == 65 and abs(i.ycor() - k.ycor()) == 65
            and spaceMatch == 0):
          spaceMatch += 1
        elif (abs(i.xcor() - k.xcor()) == 130
              and abs(i.ycor() - k.ycor()) == 130 and spaceMatch == 1):
          spaceMatch += 1
          secLastSpaceX = k.xcor()
          secLastSpaceY = k.ycor()
        elif (abs(i.xcor() - k.xcor()) == 195
              and abs(i.ycor() - k.ycor()) == 195 and spaceMatch == 2):
          spaceMatch += 1
        if (spaceMatch == 3):
          return True
    if (spaceMatch >= ultSpaceMatch):
      ultSpaceMatch = spaceMatch
      startSpaceX = i.xcor()
      startSpaceY = i.ycor()
  return [
      ultSpaceMatch, startSpaceX, startSpaceY, secLastSpaceX, secLastSpaceY
  ]


#Checking all of the ways that the bot or player could have won, then if they have won, running the function for the end of the game
def checkWins(colorSpaceList):
  if (len(colorSpaceList) >= 4):
    win = checkVertWin(colorSpaceList)
    if (win == True):
      gameWon(colorSpaceList)
    win = checkHorizWin(colorSpaceList)
    if (win == True):
      gameWon(colorSpaceList)
    win = checkDiagPosWin(colorSpaceList)
    if (win == True):
      gameWon(colorSpaceList)
    win = checkDiagNegWin(colorSpaceList)
    if (win == True):
      gameWon(colorSpaceList)


#Flashing all spaces as the winning color to show who won, then reseting the board
def gameWon(colorSpaceList):
  global openSpaceTrtlList
  global redSpaceList
  global yellowSpaceList
  index = 0
  if (colorSpaceList == redSpaceList):
    for k in range(10):
      wn.tracer(0)
      if (index % 2 == 0):
        col = 'black'
      else:
        col = 'red'
      for i in openSpaceTrtlList:
        i.color(col)
      for i in yellowSpaceList:
        i.color(col)
      for i in redSpaceList:
        i.color(col)
      index += 1
      wn.tracer(1)
      time.sleep(0.1)
  elif (colorSpaceList == yellowSpaceList):
    for k in range(10):
      wn.tracer(0)
      if (index % 2 == 0):
        col = 'black'
      else:
        col = 'yellow'
      for i in openSpaceTrtlList:
        i.color(col)
      for i in yellowSpaceList:
        i.color(col)
      for i in redSpaceList:
        i.color(col)
      index += 1
      wn.tracer(1)
      time.sleep(0.1)
  drawConnectBoard()


#Variables
#TicTacToe variables
font_setup = ("Arial", 20, "normal")
drawer = trtl.Turtle()
drawer.speed(0)
drawer.ht()
drawer.width(3)
drawTextIndicator = trtl.Turtle()
drawTextIndicator.pu()
drawTextIndicator.ht()
drawTextIndicator.goto(0, -100)
drawTextIndicator.pd()
drawTextIndicator.clear()
movesIndicator = trtl.Turtle()
movesIndicator.pu()
movesIndicator.ht()
movesIndicator.goto(-150, 50)
movesIndicator.pd()
movesIndicator.clear()
computer = trtl.Turtle()
computer.ht()
computer.pu()
computer.width(1.5)
computer.pencolor("Red")
player = trtl.Turtle()
player.ht()
player.pu()
player.width(1.5)
player.pencolor("Blue")
computerXcoords = [25, 75, 125]
computerYcoords = [130, 80, 30]
usedCoords = []
playerCoords = []
computerCoords = []
tempXcoords = 0
tempYcoords = 0
moves = 0

placementInfo = """
Placement info in coordinates:
[25, 130], [75, 130], [125, 130]
[25, 80], [75, 80], [125, 80]
[25, 30], [75, 30], [125, 30]

"""
wn = trtl.Screen()

#Connect 4 Variables
openSpaceTrtlList = []
redSpaceList = []
yellowSpaceList = []
currentColor = 'red'
wn = trtl.Screen()
turn = 0

#TicTacToe game
drawTextIndicator.write("Drawing Board...", font=font_setup)
drawTicTacToe(drawer, 50)
drawTextIndicator.clear()
print(placementInfo)
for x in range(5):
  playermove = int(input("X coord of coordinate?"))
  tempXcoords = playermove
  playermove = int(input("Y coord of coordinate?"))
  tempYcoords = playermove
  if len(usedCoords) > 0:
    while (tempXcoords, tempYcoords) in usedCoords:
      playermove = int(input("Spot used. X coord of coordinate?"))
      tempXcoords = playermove
      playermove = int(input("Spot used. Y coord of coordinate?"))
      tempYcoords = playermove
  if not tempXcoords in computerXcoords or not tempYcoords in computerYcoords:
    playermove = int(input("Invalid X coord. X coord of coordinate?"))
    tempXcoords = playermove
    playermove = int(input("Invalid Y coord. Y coord of coordinate?"))
    tempYcoords = playermove
  drawO(player, 10)
  checkForPlayerWin()
  checkForComputerWin()
  drawX(computer, 20)
  checkForPlayerWin()
  checkForComputerWin()
#Events
drawConnectBoard()

wn.listen()
wn.mainloop()



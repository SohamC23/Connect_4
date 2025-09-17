#This is the Connect 4 final project by Soham Chouhan

from random import randint
from IPython.display import clear_output #taken from M10 parctice A where it was used to clear the board before the next turn on the tic-tac-toe task
import time

def print_title():
  """
  summary line - This function prints the title of the game in fancy way using underscores, slashes, and backslashes
  args:
    no arguments/parameters
  returns:
    no returns
  """
  print("  ___  ____                    ____    ____   ___ __    /   /")
  print(" /    /   /   /\  /   /\  /   /___    /         /      /__ /")
  print("/__  /___/   /  \/   /  \/   /___    /___      /          /")
  print("                                                         /")

def printmatrix():
  """
  summary line – This function prints the board of connect 4 for the player to see
  args:
    no arguments/parameters
  returns:
    no returns
  """
  print()
  print("column number:")
  print("  1     2     3     4     5     6     7     8")
  for row in range(6):
    print(" ___   ___   ___   ___   ___   ___   ___   ___")
    for column in range(8):
      print(matrix[row][column], end=" ")
    print()

def printlogicmatrix():
  """
  summary line – This function prints the logicmatrix used to find lines of 4, or 3, or whatever. It was used a lot in testing when I needed to find out what went wrong in the program
  args:
    no arguments/parameters
  returns:
    no returns
  """
  for row in range(6):
    for column in range(8):
      print(logicmatrix[row][column], end=" ")
    print()

# 0 means the space is empty, 1 means there's an X there, and .1 will mean there is an O there
# next, I code the rules for inputs into the matrix

def row_turn(column_turn):
  """
  summary line – This function uses the column_row_list to return what row the next move in a column will go to.
  It will tell you what the row value is right above the last move played in that column.
  args:
    column_turn is the column in which the function has to find the bottommost row value
  returns:
    the row value the next move in that column should have
  """
  global column_row_list
  if (column_turn >= 0) and (column_turn < 8):
    return column_row_list[column_turn]

def row_value_updater(column_turn):
  """
  summary line – changes the column_row list by 1 so that the next move in a column doesn't overwrite the last
  args:
    the column that the last move was played in
  returns:
    none
  """
  global column_row_list
  column_row_list[column_turn] -= 1

def check_logicmatrix_win():
  """
  summary line – checks if someone has won the game
  args:
    none
  returns:
    computer or player won
  """
  global logicmatrix
  for i in range(3):
    for j in range(8):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j] + logicmatrix[i+2][j] + logicmatrix[i+3][j]), 1) == 4.0):
        return "Computer wins"
      elif (round((logicmatrix[i][j] + logicmatrix[i+1][j] + logicmatrix[i+2][j] + logicmatrix[i+3][j]), 1) == 0.4):
        return "Player wins"
  for i in range(6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 4.0):
        return "Computer wins"
      elif (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 0.4):
        return "Player wins"
  for i in range(3):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 4.0):
        return "Computer wins"
      elif (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 0.4):
        return "Player wins"
  for i in range(3,6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 4.0):
        return "Computer wins"
      elif (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 0.4):
        return "Player wins"
  return ""

# now I make functions that will help the computer read and find potencial lines that can be made into fours
def check_computer_threes():
  """
  summary line – checks if the computer has any lines of 3 it can complete to make 4-in-a-line and adds the move to the list computer_play
  if it can be played or computer_avoid if the space right under the move is open and moving there would let the player ruin the three-in-a-line
  args:
    none
  returns:
    none
  """
  global logicmatrix
  global column_row_list
  global computer_play
  global computer_avoid
  for i in range(3):
    for j in range(8):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j] + logicmatrix[i+2][j] + logicmatrix[i+3][j]), 1) == 3.0):
        computer_play.append(j)
  for i in range(6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 3.0):
        for k in range(0,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(3):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 3.0):
        for k in range(0,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(3,6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 3.0):
        for k in range(0,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""

def check_player_threes():
  """
  summary line – checks if the player has any lines of 3 it can complete to make 4-in-a-line and adds the move to the list computer_block
  if it can be played or computer_avoid if the space right under the move is open and moving there would let the player make the four-in-a-line
  args:
  descriptions of parameters
  returns:
  descriptions of return values
  """
  global logicmatrix
  global column_row_list
  global computer_block
  global computer_avoid
  for i in range(3):
    for j in range(8):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j] + logicmatrix[i+2][j] + logicmatrix[i+3][j]), 1) == 0.3):
        computer_block.append(j)
  for i in range(6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 0.3):
        for k in range(0,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(3):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 0.3):
        for k in range(0,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(3,6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 0.3):
        for k in range(0,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""

# now to make a function for making three-in-a-line-with-both-sides-open cause that can force a win for the computer
def check_computer_open_twos():
  """
  summary line – checks if the computer can turn a two into a three with both sides not blocked because that can force a win.
  If it can be played, its added to computer_play, or if the space under it is available, its added to computer_avoid.
  args:
    none
  returns:
    none
  """
  global logicmatrix
  global column_row_list
  global computer_play
  global computer_avoid
# lines going straight up can't be an open three-in-a-line, so those are ignored here
  for i in range(6):
    for j in range(4):
      if (round((logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 2) and (round((logicmatrix[i][j] + logicmatrix[i][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(2):
    for j in range(4):
      if (round((logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 2) and (round((logicmatrix[i][j] + logicmatrix[i+4][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(4,6):
    for j in range(4):
      if (round((logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 2) and (round((logicmatrix[i][j] + logicmatrix[i-4][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""

# now we check for whether the player is making three-in-a-line-with-both-sides-open so the computer can block that
def check_player_open_twos():
  """
  summary line – checks if the player can make a three with both sides open andblocks it prematurely because that can force a win.
  If it can be played, its added to computer_block, or if the space under it is available, its added to computer_avoid.
  args:
    none
  returns:
    none
  """
  global matrix
  global column_row_list
  global computer_block
  global computer_avoid
# lines going straight up can't be an open three-in-a-line, so those are ignored here
  for i in range(6):
    for j in range(4):
      if (round((logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 0.2) and (round((logicmatrix[i][j] + logicmatrix[i][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(2):
    for j in range(4):
      if (round((logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 0.2) and (round((logicmatrix[i][j] + logicmatrix[i+4][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(4,6):
    for j in range(4):
      if (round((logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 0.2) and (round((logicmatrix[i][j] + logicmatrix[i-4][j+4]), 1) == 0):
        for k in range(1,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_block.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""

def check_computer_closed_two():
  """
  summary line – Checks if the computer can make any twos into threes that have enough space to become fours
  If it can be played, its added to computer_play, or if the space under it is avialable, its added to computer_avoid.
  args:
    none
  returns:
    none
  """
  global logicmatrix
  global column_row_list
  global computer_play
  global computer_avoid
  for i in range(3):
    for j in range(8):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j] + logicmatrix[i+2][j] + logicmatrix[i+3][j]), 1) == 2.0):
        computer_play.append(j)
  for i in range(6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 2.0):
        for k in range(0,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(3):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 2.0):
        for k in range(0,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(3,6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 2.0):
        for k in range(0,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""

def check_computer_closed_one():
  """
  summary line – finds ones that can be made into twos with enough space to be a potential four.
  If it can be played, its added to computer_play, or if the space under it is avialable, its added to computer_avoid.
  args:
    none
  returns:
    none
  """
  global logicmatrix
  global column_row_list
  global computer_play
  global computer_avoid
#ignoring straight up and down 4s in a line because those are unlikly to work but are usually available and would make bad moves
  for i in range(6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i][j+1] + logicmatrix[i][j+2] + logicmatrix[i][j+3]), 1) == 1.0):
        for k in range(0,4):
          if logicmatrix[i][j+k] == 0:
            if column_row_list[j+k] == i:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+1:
              computer_avoid.append(j+k)
  for i in range(3):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i+1][j+1] + logicmatrix[i+2][j+2] + logicmatrix[i+3][j+3]), 1) == 1.0):
        for k in range(0,4):
          if logicmatrix[i+k][j+k] == 0:
            if column_row_list[j+k] == i+k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i+k+1:
              computer_avoid.append(j+k)
  for i in range(3,6):
    for j in range(5):
      if (round((logicmatrix[i][j] + logicmatrix[i-1][j+1] + logicmatrix[i-2][j+2] + logicmatrix[i-3][j+3]), 1) == 1.0):
        for k in range(0,4):
          if logicmatrix[i-k][j+k] == 0:
            if column_row_list[j+k] == i-k:
              computer_play.append(j+k)
            elif column_row_list[j+k] == i-k+1:
              computer_avoid.append(j+k)
  return ""


# challenge!: make a function for the bot to make a 3/4 trap and zugzwang. ---  Update: 3/4 trap and zugzwang havent been coded in becuase I have yet to figure out how to do so

#since defining functions are done, first, I create the logic matrix that the rest of the program will manipulate

'''
I am copying an example of a matrix made using forloops to use as a referance, the matrix was taken from https://www.geeksforgeeks.org/python-matrix/:
This matrix takes user input to make the matrix

Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):
    a = []
# A for loop for column entries
    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()
'''

# Now I adapt the referance to make my logic Matrix for the 6x8 board,
matrix = []
for row in range(6):
  a = []
  # A for loop for column entries
  for column in range(8):
    a.append(" [_] ")
  matrix.append(a)

logicmatrix = []
for row in range(6):
  a = []
  for column in range(8):
    a.append(0)
  logicmatrix.append(a)

column_row_list = [5, 5, 5, 5, 5, 5, 5, 5]  #This list holds the row value of the bottommost space in a row of the matrix that is available. For example, column_row_list[0] means that column 0's bottommost available value has a row value of 5
print_title()#asthetics and display
print()
printmatrix()
print()
while True:#lets player decide to go first or second
  player = input("Enter \"1\" to go first, or \"2\" to go second: ")
  if player == "1" or player == "2":
    player = int(player)
    computer = player % 2 + 1 #sets computer to other number not chosen by the player
    break
  else:
    print("That wasn't a \"1\" or a \"2\"! Try again!")
turn = 1
game = "ongoing"
while game != "fin":
  if turn==computer:
    '''
    order of importance for moves is: --- making 3 into 4 --- stopping opponent 3 into 4 --- not playing the move right below opponents 3 to let them make a 4 next move
    --- stopping opponent from making an open 3 trap --- not making a move that lets oppnent make an open 3 trap --- playing the move to make an open two into and open 3 trap
    --- making closed 3s --- setting up an open 2 to make an open 3 trap --- making open 2s that can become closed 3s --- random move into an open spot to make open 2s

    challenge: make 3/4 trap, zugzwang (unfinished)

    '''

    computer_play = []#emptying all lists before new move
    computer_block = []
    computer_avoid = []
    computer_play_options = []
    check_computer_threes()#making 3s into 4s
    if computer_play != []:
      computer_play_options.append(computer_play[0])
    else:
      check_player_threes()#blocking player 3s into 4s
      if computer_block != []:
        computer_play_options.append(computer_block[0])
      else:
        check_player_open_twos()# checking for potential open three traps and blocking beforehand
        computer_avoid_upper_bound = len(computer_block)
        for x in range(0, computer_avoid_upper_bound):
          if (computer_block[-x + computer_avoid_upper_bound - 1] in computer_avoid):#checking if blocking the open two will give the player a winning move
            del computer_block[-x + computer_avoid_upper_bound - 1]
        if (computer_block != []):
          computer_play_options.extend(computer_block)
        else:
          check_computer_open_twos()#completing an open three trap
          computer_avoid_upper_bound = len(computer_play)
          for x in range(0, computer_avoid_upper_bound):
            if (computer_play[-x + computer_avoid_upper_bound - 1] in computer_avoid):#checking if making the open two will give the player a winning move
              del computer_play[-x + computer_avoid_upper_bound - 1]
          if (computer_play != []):
            computer_play_options.extend(computer_play)
          else:
            check_computer_closed_two()#making normal 2s into 3s
            computer_avoid_upper_bound = len(computer_play)
            for x in range(0, computer_avoid_upper_bound):
              if (computer_play[-x + computer_avoid_upper_bound - 1] in computer_avoid):#checking if making the three will give the player a better move and should be avoided
                del computer_play[-x + computer_avoid_upper_bound - 1]
            if (computer_play != []):
              computer_play_options.extend(computer_play)
            else:
              check_computer_closed_one()#making possible 1s into 2s
              computer_avoid_upper_bound = len(computer_play)
              for x in range(0, computer_avoid_upper_bound):
                if (computer_play[-x + computer_avoid_upper_bound - 1] in computer_avoid):#checking if making the two will give the player a better move and should be avoided
                  del computer_play[-x + computer_avoid_upper_bound - 1]
              if (computer_play != []):
                computer_play_options.extend(computer_play)
              else:
                for x in range(0,8):#making any move into any column
                  if x not in computer_avoid:# checking if making that move will give the player a better move and should be avoided
                    computer_play_options.append(x)
    for x in range(0,18):
      computer_move = computer_play_options[randint(0,len(computer_play_options)-1)]#chooses random value from computer_play_options
      if (row_turn(computer_move)>=0):#checks if the column is available
        break
      elif (x >= 10): #starts trying each column to see if its empty in the event that nothing from computer_play_optons is viable
        computer_move = x-10
        if (row_turn(computer_move)>=0):# if a column is empty, the move is kept
          break
    time.sleep(.5)#this makes the computers move time less jarring and helps avoid glitches regarding inputs
    matrix[row_turn(computer_move)][computer_move] = " [X] "
    logicmatrix[row_turn(computer_move)][computer_move] = 1.0
    if (check_logicmatrix_win().startswith("Computer wins")):
      game = "fin"
    print()
    row_value_updater(computer_move)#makes the next move in the column go into the row right above this move rather then overwriting this move
    clear_output()#clears the board
    print_title()
    print()
    print("computer's last move was in column %s"%(computer_move + 1))#tells the player the last move for clarity
    printmatrix()
    turn=player#makes the next turn the players
  elif turn==player:
    try:
      player_move = (int(input("Player (0), enter in the column number of your move: ")) - 1)
      if(player_move >= 0) and (player_move < 8): #makes sure the input is a number between 1-8
        print()
        if (row_turn(player_move) >= 0):#makes sure the column being moved into isn't full
          matrix[row_turn(player_move)][player_move] = " [0] "#puts move into the board
          logicmatrix[row_turn(player_move)][player_move] = 0.1#puts move into the logicmatrix that all the functions read
          if (check_logicmatrix_win().startswith("Player wins")):#checks for a win
            game = "fin"
          row_value_updater(player_move)#makes the next move in the column go into the row right above this move rather then overwriting this move
          turn=computer#makes the next turn the computers
        else:
          print()
          print("column is full")
      else:
        print()
        print("only enter column numbers from 1 to 8")
    except ValueError:#accounts for inputs other than integers
      print()
      print("only enter in integers 1-8 for the column number")
  if (column_row_list == [-1, -1, -1, -1, -1, -1, -1, -1]) and (check_logicmatrix_win().startswith("")): #checks if the board is full and no one has won (tie)
    game = "fin"
clear_output()
print_title()
print()
printmatrix()
print()
if (check_logicmatrix_win().startswith("Computer wins")):
  print("Computer wins, womp womp!")
elif (check_logicmatrix_win().startswith("Player wins")):
  print("Player wins, congrats!")
elif (column_row_list == [-1, -1, -1, -1, -1, -1, -1, -1]) and (check_logicmatrix_win().startswith("")):
  print("Tie game, well played!")
else:#in case if something goes horribly wrong
  print("Due to technical difficulties, no one won")
print()
print("thanks for playing!")
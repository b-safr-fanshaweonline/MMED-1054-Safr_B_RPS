# Rock Paper Scissors
# 
# PREREQUISITES
# GAME
# - playAgain()
# - launchWelcome()
# - launchGame()
# INIT
# - launchWelcome()
# - launchGame()


#-----------------------------------------------------------------------

# PREREQUISITES

# used for computer choice
from random import randint

# import game variables
from gameComponents import gameVars, display, winLose

#-----------------------------------------------------------------------

# GAME

# playAgain

def resetGame():
  gameVars.computer_lives = gameVars.total_lives
  gameVars.player_lives = gameVars.total_lives
  launchGame()

def playAgain():
  print(
    display.line(""),
    display.line("Play Again (y/n)?"),
    sep='\n')
  player_choice = input("| ->")
  if (player_choice[0] == "Y" or 
    player_choice[0] == "y"):
    resetGame()
  else:
    quit()

# launchWelcome

def launchWelcome():
  print(
    display.border(),
    display.line(""),
    display.line("Welcome to Rock Paper Scissors!"),
    display.line(""),
    sep='\n')

# launchGame

def playerChoice(prompt):
  print(
    display.line(""),
    display.line(prompt),
    display.line(""),
    display.line("  Type '1' or 'r' for Rock"),
    display.line("  Type '2' or 'p' for Paper"),
    display.line("  Type '3' or 's' for Scissors"),
    display.line(""),
    display.line("  Or submit nothing to exit"),
    sep='\n')
  player_choice = input("| -> ")
  if (player_choice == ""):
    quit()
  elif (player_choice[0] == "R" or 
    player_choice[0] == "r" or
    player_choice == "1"):
    return 1
  elif (player_choice[0] == "P" or 
    player_choice[0] == "p" or
    player_choice == "2"):
    return 2
  elif (player_choice[0] == "S" or 
    player_choice[0] == "s" or
    player_choice == "3"):
    return 3
  else:
    return playerChoice("Sorry, didn't understand '"+ player_choice+"'")


def launchGame():
  print(
    display.line("Round: "+str(gameVars.round_counter)),
    sep='\n')

  # Get Player Choice

  player_choice = playerChoice("Please choose:")

  # Get Computer Choice

  computer_choice = randint(1, 3)

  # Get Winner

  win_state = winLose.roundWinner(player_choice,computer_choice)

  # Lose a Life

  if (win_state == 0):
    gameVars.player_lives = gameVars.player_lives - 1
  elif (win_state == 1):
    gameVars.computer_lives = gameVars.computer_lives - 1

  display.round(
    player_choice ,
    computer_choice ,
    win_state
    )

  if (gameVars.computer_lives > 0 and gameVars.player_lives > 0):
    gameVars.round_counter = gameVars.round_counter + 1
    launchGame()
  else:
    if (gameVars.player_lives == 0):
      display.victory(0)
      playAgain()
    elif (gameVars.computer_lives == 0):
      display.victory(1)
      playAgain()

#-----------------------------------------------------------------------

# Init

launchWelcome()
launchGame()

#-----------------------------------------------------------------------
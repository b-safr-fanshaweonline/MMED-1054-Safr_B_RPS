# Rock Paper Scissors
# 
# PREREQUISITES
# GAME
# INIT


#-----------------------------------------------------------------------

# PREREQUISITES

# used for computer choice
from random import randint

# import game variables
from gameComponents import display, gameVars, winLose

#-----------------------------------------------------------------------

# GAME

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

def launchGame():
  display.round(gameVars.round_counter,gameVars.user_wins,gameVars.comp_wins)
  display.lives(gameVars.computer_lives,gameVars.player_lives,gameVars.total_lives)

  # Get Player Choice

  player_choice = display.choice("Please choose:")

  # Get Computer Choice

  computer_choice = randint(1, 3)

  # Get Winner

  win_state = winLose.winner(player_choice,computer_choice)

  # Lose a Life

  if (win_state == 0):
    gameVars.player_lives = gameVars.player_lives - 1
  elif (win_state == 1):
    gameVars.computer_lives = gameVars.computer_lives - 1

  # Play the Round

  display.gameRound(
    player_choice ,
    computer_choice ,
    win_state
    )

  # Deterimne Victor
  # - if none, play another round

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

display.welcome()
launchGame()

#-----------------------------------------------------------------------
# Display
# 
# - standardize at 80 characters wide
# 
# LINE
# - print a line of text capped with "|"
# BORDER
# - print a horizontal line
# LIVES
# - print lives
# GAME
# - print the whole rock paper scissors game


# used for animation timing
import time

from gameComponents import gameVars

def line(content):
  return("| " + content + (" " * ( 76 - len(content) )) + " |")

def border():
  return(".==============================================================================.")

def lives():
  print(
    line(""),
    line("Computer Lives: "+ str(gameVars.computer_lives) +"/"+ str(gameVars.total_lives)),
    line("Player Lives: "+ str(gameVars.player_lives) +"/"+ str(gameVars.total_lives)),
    line(""),
    sep='\n')

def round(player_choice, computer_choice, win_state):

  rock = "    R O C K    "
  paper = "   P A P E R   "
  scissors = "S C I S S O R S"

  # format player choice
  if (player_choice == 1):
    player_choice = rock
  elif (player_choice == 2):
    player_choice = paper
  elif (player_choice == 3):
    player_choice = scissors

  # format computer choice
  if (computer_choice == 1):
    computer_choice = rock
  elif (computer_choice == 2):
    computer_choice = paper
  elif (computer_choice == 3):
    computer_choice = scissors


  def dramatic_pause():
    pause_length = .400
    time.sleep(pause_length)
    print(line("                 ."), end="\r")
    time.sleep(pause_length)
    print(line("                 . ."), end="\r")
    time.sleep(pause_length)
    print(line("                 . . ."), end="\r")
    time.sleep(pause_length)

  time.sleep(.800)

  print(
    line(""),
    line(""),
    line(""),
    line("      ......"),
    line("     /\\|||||\\"),
    line("     \\      |"),
    line("      \\    /"),
    line("      |    |"),
    line("  "+ rock + " !"),
    sep='\n')

  dramatic_pause()

  print(
    line("       .."),
    line("     ||||||.."),
    line("     ||||||||"),
    line("    .||||||||"),
    line("    ||      |"),
    line("    \\\\      |"),
    line("     \\      /"),
    line("      |    |"),
    line("  "+ paper + " !"),
    sep='\n')

  dramatic_pause()

  print(
    line(""),
    line("     ||  //"),
    line("     || //"),
    line("     ||//..."),
    line("     |.. |||\\"),
    line("     \\      |"),
    line("      \\     /"),
    line("      |    |"),
    line("  "+ scissors + " !"),
    sep='\n')

  time.sleep(.800)

  # ANNOUNCE WINNER

  print(
    line(""),
    line("  You played:"),
    sep='\n')

  time.sleep(.800)

  print(
    line(""),
    line("    - - - - - - - -  "),
    line("  | "+ player_choice +" |"),
    line("    - - - - - - - -  "),
    sep='\n')

  time.sleep(.800)

  print(
    line(""),
    line("  Computer played:"),
    sep='\n')

  time.sleep(.800)

  print(
    line(""),
    line("    - - - - - - - -  "),
    line("  | "+ computer_choice +" |"),
    line("    - - - - - - - -  "),
    sep='\n')

  time.sleep(.800)

  win_you = "       Y O U   W I N       "
  win_comp = " C O M P U T E R   W I N S "
  tie_game = "      T I E   G A M E      "

  if (win_state == 0):
    winner = win_comp
  elif (win_state == 1):
    winner = win_you
  elif (win_state == 2):
    winner = tie_game

  print(
    line(""),
    line("    - - - - - - - - - - - - -  "),
    line("  |"+ winner + "|"),
    line("    - - - - - - - - - - - - -  "),
    sep='\n')

  time.sleep(.800)

  lives()

  time.sleep(.800)

def victory(win_state):

  win_you = "       Y O U   W I N       "
  win_comp = " C O M P U T E R   W I N S "

  if (win_state == 0):
    winner = win_comp
    message = "You are out of lives!"
  elif (win_state == 1):
    winner = win_you
    message = "Computer is out of lives!"

  print(
    line(message),
    line(""),
    line("    ! ! ! ! ! ! ! ! ! ! ! ! !  "),
    line("  !"+ winner + "!"),
    line("    ! ! ! ! ! ! ! ! ! ! ! ! !  "),
    line(""),
    border(),
    sep='\n')
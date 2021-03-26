# Display
# 
# - standardize at 80 characters wide
# 
# PREREQUISITES
# BASICS
# - line()
#   - display a line of text capped with "|" at the ends
# - border()
#   - display a horizontal line
# - welcome()
#   - display welcome message
# - round()
#   - display current round count
# - lives()
#   - display current lives counts
# PLAYER INPUT
# - choice()
# GAME ROUND
# - gameRound()
# VICTORY
# - victory()
# Line
# Line

#-----------------------------------------------------------------------

# PREREQUISITES

# used for animation timing
import time

# golbal variables for later
rock = "    R O C K    "
paper = "   P A P E R   "
scissors = "S C I S S O R S"
win_you = "       Y O U   W I N       "
win_comp = " C O M P U T E R   W I N S "
tie_game = "      T I E   G A M E      "

#-----------------------------------------------------------------------

# BASICS

def line(content):
  return("| " + content + (" " * ( 76 - len(content) )) + " |")

def border():
  return("|==============================================================================|")

def welcome():
  print(
    border(),
    line(""),
    line("Welcome to Rock Paper Scissors!"),
    sep='\n')

def round(round_num,user_wins,comp_wins):
  print(
    line(""),
    line("Round: "+str(round_num)),
    line(""),
    line("User Wins: "+str(user_wins)),
    line("Computer Wins: "+str(comp_wins)),
    sep='\n')

def lives(computer_lives,player_lives,total_lives):
  print(
    line(""),
    line("Computer Lives: "+ str(computer_lives) +"/"+ str(total_lives)),
    line("Player Lives: "+ str(player_lives) +"/"+ str(total_lives)),
    line(""),
    sep='\n')
  time.sleep(.800)

#-----------------------------------------------------------------------

# PLAYER INPUT

def choice(prompt):
  print(
    line(""),
    line(prompt),
    line(""),
    line("  Type '1' or 'r' for Rock"),
    line("  Type '2' or 'p' for Paper"),
    line("  Type '3' or 's' for Scissors"),
    line(""),
    line("  Or submit nothing to exit"),
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
    return choice("Sorry, didn't understand '"+ player_choice+"'")

#-----------------------------------------------------------------------

# GAME ROUND

def gameAnimation():

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

def gameRound(player_choice, computer_choice, winner):

  # Display Animation

  gameAnimation()

  # Announce Winner

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

  # format winner

  if (winner == 0):
    winner = win_comp
  elif (winner == 1):
    winner = win_you
  elif (winner == 2):
    winner = tie_game

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

  print(
    line(""),
    line("    - - - - - - - - - - - - -  "),
    line("  |"+ winner + "|"),
    line("    - - - - - - - - - - - - -  "),
    sep='\n')

  time.sleep(.800)

#-----------------------------------------------------------------------

# VICTORY

def victory(winner):

  win_you = "       Y O U   W I N       "
  win_comp = " C O M P U T E R   W I N S "

  if (winner == 0):
    winner = win_comp
    message = "You are out of lives!"
  elif (winner == 1):
    winner = win_you
    message = "Computer is out of lives!"

  time.sleep(.800)

  print(
    line(message),
    line(""),
    line("    ! ! ! ! ! ! ! ! ! ! ! ! !  "),
    line("  !"+ winner + "!"),
    line("    ! ! ! ! ! ! ! ! ! ! ! ! !  "),
    line(""),
    border(),
    sep='\n')

  time.sleep(.800)

#-----------------------------------------------------------------------
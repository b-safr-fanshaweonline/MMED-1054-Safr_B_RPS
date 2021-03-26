def roundWinner(player_choice,computer_choice):
  # return:
  # 0 = computer wins
  # 1 = player wins
  # 2 = tie game

  # assume a tie game
  win_state = 2

  # DETERMINE WINNER

  # computer makes random choice
  # 1 = rock
  # 2 = paper
  # 3 = scissors

  # if computer is rock
  if (computer_choice == 1):
    
    # and player is paper
    if (player_choice == 2):
      win_state = 1
      # player wins

    # unless player is scissors
    elif (player_choice == 3):
      win_state = 0
      # computer wins

  # or, if computer is paper
  elif (computer_choice == 2):
    
    # and player is scissors
    if (player_choice == 3):
      win_state = 1
      # player wins

    # unless player is rock
    elif (player_choice == 1):
      win_state = 0
      # computer wins

  # or, if computer is scissors
  elif (computer_choice == 3):
    
    # and player is rock
    if (player_choice == 1):
      win_state = 1
      # player wins

    # unless player is paper
    elif (player_choice == 2):
      win_state = 0
      # computer wins

  return win_state

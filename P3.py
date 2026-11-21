board = [" " for _ in range(9)]

def display():
  print()
  print(board[0],"|") #Defining the board
  
def display_board(board):
  print()
  print(board[0], '|', board[1], '|', board[2])
  print('---------')
  print(board[3], '|', board[4], '|', board[5])
  print('---------')
  print(board[6], '|', board[7], '|', board[8])
  print()
  
def check_win(board, player):
  # Check rows
  for i in range(0, 9, 3):
    if board[i] == board[i+1] == board[i+2] == player:
      return True
  # Check columns
  for i in range(3):
    if board[i] == board[i+3] == board[i+6] == player:
      return True
  # Check diagonals
  if board[0] == board[4] == board[8] == player:
    return True
  if board[2] == board[4] == board[6] == player:
    return True
  return False

def check_draw(board):
  return ' ' not in board and not (check_win(board, 'X') or check_win(board, 'O'))

def minimax(board, depth, is_maximizing):
  if check_win(board, 'O'):  # AI wins
    return 1
  if check_win(board, 'X'):  # Player wins
    return -1
  if check_draw(board):
    return 0

  if is_maximizing:
    best_score = -float('inf')
    for i in range(9):
      if board[i] == ' ':
        board[i] = 'O'
        score = minimax(board, depth + 1, False)
        board[i] = ' ' # Undo the move
        best_score = max(score, best_score)
    return best_score
  else:
    best_score = float('inf')
    for i in range(9):
      if board[i] == ' ':
        board[i] = 'X'
        score = minimax(board, depth + 1, True)
        board[i] = ' ' # Undo the move
        best_score = min(score, best_score)
    return best_score

def ai_move(board):
  best_score = -float('inf')
  best_move = -1
  for i in range(9):
    if board[i] == ' ':
      board[i] = 'O'
      score = minimax(board, 0, False)
      board[i] = ' ' # Undo the move
      if score > best_score:
        best_score = score
        best_move = i
  board[best_move] = 'O'

def player_move(board):
  while True:
    try:
      move = int(builtins.input("Enter your move (0-8): "))
      if 0 <= move <= 8 and board[move] == ' ':
        board[move] = 'X'
        break
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def play_game():
  board = [' ' for _ in range(9)]
  current_player = 'X' # X for human, O for AI

  print("Welcome to Tic Tac Toe!")
  display_board(board)

  while True:
    if current_player == 'X':
      player_move(board)
    else:
      print("AI's turn...")
      ai_move(board)

    display_board(board)

    if check_win(board, 'X'):
      print("You win!")
      break
    elif check_win(board, 'O'):
      print("AI wins!")
      break
    elif check_draw(board):
      print("It's a draw!")
      break

    current_player = 'O' if current_player == 'X' else 'X'

import builtins
play_game()

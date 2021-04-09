import os



board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]] 


def tic_tac_toe():
  while True:
    play_single_game()

    print("\n")
    answer = ""
    while not answer in ["y", "n"]:
      answer = input("would you like to play again? (y/n)\n")
    if answer == "y":
      clear_board()
      continue
    if answer == "n":
      break

def play_single_game():
  print("TIC TAC TOE\n\n")
  
  #using for loop (instead of while) so i have access to loop index
  for turn in range(0, 10):
    os.system('cls' if os.name == 'nt' else 'clear')
    render_board()
    
    if check_for_win(): 
      print(f"{check_for_win()} wins!")
      return
    elif turn == 9:
      print("no winner 😭")
      return
    
    player = "X" if turn % 2 == 0 else "O"
    get_move(player)




def render_board ():
  global board 

  unpacked_board = [i for sub in board for i in sub]
  a, b, c, d, e, f, g, h, i = unpacked_board
      
  print(f"""
       1   2   3
    1  {a} | {b} | {c}
      ---|---|---
    2  {d} | {e} | {f}
      ---|---|---
    3  {g} | {h} | {i}
    """)



def get_move(player):
  global board 

  print(f"player {player}'s turn:")

  valid_move = False

  while not valid_move:
    row = get_integer("row:", [1, 2, 3]) - 1 
    column = get_integer("column:", [1, 2, 3]) - 1
    
    if board[row][column] == " ":
      valid_move = True
    else:
      print("invalid move")

  board[row][column] = player
  return

def get_integer(prompt, valid_arr):
  while True:
    try:
      answer = int(input(prompt))
    except ValueError:
      print("invalid input")
      continue
    
    if answer in valid_arr: 
      break

  return answer



def check_for_win():
  if check_for_straight_win():
    return check_for_straight_win()
  
  if check_for_diagonal_win():
    return check_for_diagonal_win()

def check_for_straight_win():
  global board 

  # horizontal win
  for row in board:
    if not " " in row and len(set(row)) == 1:
      return row[0]

  # vertical win
  for i in range(0, 3):
    column = [row[i] for row in board]
    if not " " in column and len(set(column)) == 1:
      return column[0]

  return False

def check_for_diagonal_win():
  global board 

  if not board[1][1] == " " and (len(set([board[0][0], board[1][1], board[2][2]])) == 1 or len(set([board[0][2], board[1][1], board[2][0]])) == 1):
    # both diagonal wins require the middle position
    return board[1][1]
  return False



def clear_board():
  global board 
  board = [[" " for j in range(0,3)] for i in range(0,3)]



tic_tac_toe()
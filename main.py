import os

# TODO:
# def render_board
# def get_input
# def check_for_win


board_positions = [[" ", " ", " "], 
                   [" ", " ", " "], 
                   [" ", " ", " "]]

def render_board ():
  unpacked_board_positions = [i for sub in board_positions for i in sub]
  a, b, c, d, e, f, g, h, i = unpacked_board_positions

      
  print(f"""
       1   2   3
    1  {a} | {b} | {c}
      ---|---|---
    2  {d} | {e} | {f}
      ---|---|---
    3  {g} | {h} | {i}
    """)

def get_move(player):

  print(f"player {player}'s turn:")

  valid_move = False

  while not valid_move:
    row = get_input("row:", [1, 2, 3]) - 1 
    column = get_input("column:", [1, 2, 3]) - 1
    
    if board_positions[row][column] == " ":
      valid_move = True
    else:
      print("invalid move")

  board_positions[row][column] = player
  return


def get_input(prompt, valid_arr):
  while True:
    try:
      answer = int(input(prompt))
    except ValueError:
      print("invalid input, type 1, 2 or 3")
      continue
    
    if answer in valid_arr: 
      break

  return answer

def play_game():
  print("TIC TAC TOE\n\n")
  #using for loop (instead of while) so i have access to loop index
  for turn in range(0, 9):
    os.system('cls' if os.name == 'nt' else 'clear')

    render_board()
    player = "X" if turn % 2 == 0 else "O"

    get_move(player)

    if check_for_win(): 
      print(f"{check_for_win()} wins!")



def check_for_win():

  return False





# while not winner_exists():
  # get_move()




# testing
#----------------------------

play_game()
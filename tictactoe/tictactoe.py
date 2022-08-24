import random
import time

class Player: 
  def __init__(self, name, mark):
    self.mark = mark
    self.name = name

  def get_name(self):
    """
    Displays player name
    """

    return self.name

  def get_mark(self):
    """
    Get the player mark
    """

    return self.mark

class Computer(Player):
  def __init__(self, name, mark):
    super().__init__(name, mark)

  def get_mark(self):
    """
    Get the player mark
    """

    return self.mark

  def make_turn(self, board, validate):
    """
    Computers turn
    """

    while True:
      random_pick = random.randint(0, 8)
      if validate(random_pick):
        board[random_pick] = self.get_mark()
        break

class TicTacToe:
  def __init__(self, computer=True):
    self.board = [" " for _ in range(0, 9)]
    self.computer = computer

  def draw_board(self):
    """
    Draws a 3x3 grid that is going to be the board of the game
    """
    
    for b in range(len(self.board)):
      print(" | " + self.board[b] + " | ", end="")
      if (b + 1) % 3 == 0:
        print("\n")

  def is_turn_valid(self, spot):
    if self.board[spot] == " ":
      return True
    return False

  def is_winner(self, turn):
    """
    Checks whether current player/computer wins
    
    Checks for horizontal, vertical, and diagonal patter ns of the board
    """
    
    # Checks for horizontal pattern
    h_start, h_end = 0, 3
    for h in range(int(len(self.board) / 3)):
      if set(self.board[h_start:h_end]) == set(turn):
        return True
      h_start, h_end = h_start + 3, h_end + 3

    # Checks for vertical pattern
    v_start, v_end = 0, 7
    for v in range(int(len(self.board) / 3)):
      if set(self.board[v_start:v_end:3]) == set(turn):
        return True
      v_start, v_end = v_start + 1, v_end + 1

    # Checks for diagonal pattern (0, 4, 8) 
    if set(self.board[0:9:4]) == set(turn):
      return True

    # Checks for diagonal pattern (2, 4, 6) 
    if set(self.board[2:7:2]) == set(turn):
      return True
      
    return False

  def is_draw(self):
    """
    Determines whether its a draw for both players
    """
    
    if " " not in self.board:
      return True
    return False

  def play(self):
    r"""
    ==============================================================
     _   _      _             _             
    | | (_)    | |           | |            
    | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
    | __| |/ __| __/ _` |/ __| __/ _ \ / _ \
    | |_| | (__| || (_| | (__| || (_) |  __/
    \__|_|\___|\__\__,_|\___|\__\___/ \___|

    ==============================================================

    RULES FOR TIC-TAC-TOE: 

     - The game is played on a grid that's 3 squares by 3 squares.
     - You are X, your friend (or the computer in this case) is O. ...
     - The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
     - When all 9 squares are full, the game is over.

    """

    if self.computer:
      player = Player(name="Player", mark="X") # Create instance of the player
      computer = Computer(name="Computer", mark="O") # Create instance of the computer

      # Player turn
      while True:
        turn = input("You're turn, choose from 0 - 8: ")
        if turn.isdigit():
          if int(turn) >= 0 and int(turn) <= 8:
            if self.is_turn_valid(int(turn)):
              self.board[int(turn)] = player.get_mark()
              self.draw_board()

              if self.is_draw():
                print("It's a draw.")
                break
              elif self.is_winner(player.get_mark()):
                print("{} wins.".format(player.get_name()))
                break
              # Computer turn
              print("Computer's turn ... ")
              time.sleep(1.5)
              computer.make_turn(self.board, self.is_turn_valid)
              self.draw_board()

              if self.is_draw():
                print("It's a draw.")
                break
              elif self.is_winner(computer.get_mark()):
                print("{} wins.".format(computer.get_name()))
                break
            else:
              print("Invalid turn!")
          else:
            print("Choose from 0 - 8 only!")
        else:
          print("Please input a valid number!")
    else:
      player_one = Player(name="Player One", mark="X") # Creates an instance of player one
      player_two = Player(name="Player Two", mark="O") # Creates an instance of player two

      while True:
        turn = input("{}'s turn, choose from 0 - 8: ".format(player_one.get_name()))
        if turn.isdigit():
          if int(turn) >= 0 and int(turn) <= 8:
            if self.is_turn_valid(int(turn)):
              self.board[int(turn)] = player_one.get_mark()
              self.draw_board()

              if self.is_draw():
                print("It's a draw.")
                break
              elif self.is_winner(player_one.get_mark()):
                print("{} wins.".format(player_one.get_name()))
                break
              # Player two's turn
              print()
              turn = input("{}'s turn, choose from 0 - 8: ".format(player_two.get_name()))
              if turn.isdigit():
                if int(turn) >= 0 and int(turn) <= 8:
                  if self.is_turn_valid(int(turn)):
                    self.board[int(turn)] = player_two.get_mark()
                    self.draw_board()
                    if self.is_draw():
                      print("It's a draw.")
                      break
                    elif self.is_winner(player_two.get_mark()):
                      print("{} wins.".format(player_two.get_name()))
                      break
                  else:
                    print("Invalid turn!")
                    continue
                else:
                  print("Choose from 0 - 8 only!")
              else:
                print("Please input a valid number!")
            else:
              print("Invalid turn!")
          else:
            print("Choose from 0 - 8 only!")
        else:
          print("Please input a valid number!")

t = TicTacToe(computer=False)
print(t.play.__doc__)
t.play()
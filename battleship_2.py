from random import randint



def print_board(board):
  for row in board:
    print(' '.join(row))




def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)


def play():
    board = []

    for x in range(0, 5):
        board.append(["O"] * 5)

    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)



    for turn in range(4):
        print("Turn : ",turn+1)
        guess_row = input("Guess Row: ")
        guess_col = input("Guess Col: ")

        if guess_row == ship_row and guess_col == ship_col:
            print( "Congratulations! You sank my battleship!")
            break
        elif guess_row == "#" and guess_col == "#":
            print( "---------------Easter Egg!!!-------------------")
            board[ship_row][ship_col]="#"
            print_board(board)
            break
        else:
            guess_row = int(guess_row)
            guess_col = int(guess_col)
            if (guess_row not in range(5) or  guess_col not in range(5)):
                print( "Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print( "You guessed that one already." )
            else:
                print( "You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if (turn == 3):
                print( "------------Game Over--------------")
                print("Answer>>>>> Row is",ship_row,"Column is",ship_col)
                board[ship_row][ship_col]="#"
                
            print_board(board)


def main():
    play()
    while input("Play again ? (Y/N_) ").upper()== "Y":
        play()



if (__name__=="__main__"):
   main()


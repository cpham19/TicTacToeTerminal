import random


class TicTacToe():
    def __init__(self):
        self.newGame()
        self.startGame()

    def printGame(self):
        for row in range(0, len(self.gameboard)):
            for col in range(0, len(self.gameboard[row])):
                print(str(self.gameboard[row][col]), end=" ")

            print()

    def playerMove(self):
        move = None

        while (move == None):
            userInput = input("Type your move (in the form of # #, for example 1 1 would be in Row #1 and Column #1)\n")

            # Validating user input
            if (len(userInput) == 3 and userInput[0].isdigit() and userInput[2].isdigit() and int(
                    userInput[0]) >= 1 and int(userInput[0]) <= 3 and int(userInput[2]) >= 1 and int(
                    userInput[2]) <= 3):
                move = userInput

                row = int(move[0]) - 1
                col = int(move[2]) - 1

                if (self.gameboard[row][col] == 0):
                    self.gameboard[row][col] = self.playerMark
                    self.turns = self.turns + 1
                    self.playerTurn = "CPU's Turn"

                else:
                    print("Invalid move: The square is occupied.\n")
                    self.printGame()
                    move = None
            else:
                print("Invalid input: Minimum value allowed is 1 and Maximum Value allowed is 3!\n")
                self.printGame()

    def botMove(self):
        randomRow = random.randint(0, 2)
        randomCol = random.randint(0, 2)

        while (self.gameboard[randomRow][randomCol] != 0):
            randomRow = random.randint(0, 2)
            randomCol = random.randint(0, 2)

        print("Bot's move: " + str(randomRow) + " " + str(randomCol))

        self.gameboard[randomRow][randomCol] = self.cpuMark
        self.turns = self.turns + 1
        self.playerTurn = "Player's Turn"



    def startGame(self):
        self.newGame()
        while (self.checkState()['state'] is False and self.turns != 9):
            self.printGame()
            if (self.playerTurn == "Player's Turn"):
                self.playerMove()
            else:
                self.botMove()

            print()

        if (self.checkState()['state'] is False and self.turns == 9):
            self.printGame()
            print("It's a draw!!!")
        elif (self.checkState()['state'] is True):
            self.printGame()
            print(self.checkState()['playerWon'] + " won the game!")
            

    def checkState(self):
        stateObj = {'state': False, 'playerWon': "None"}
        # for 1
        # Check if one of the three rows have three 1's
        if ((self.gameboard[0][0] == 1 and self.gameboard[0][1] == 1 and self.gameboard[0][2] == 1) or
            (self.gameboard[1][0] == 1 and self.gameboard[1][1] == 1 and self.gameboard[1][2] == 1) or
            (self.gameboard[2][0] == 1 and self.gameboard[2][1] == 1 and self.gameboard[2][2] == 1)
            # Check if one of the three columns have three 2's
            or (self.gameboard[0][0] == 1 and self.gameboard[1][0] == 1 and self.gameboard[2][0] == 1) or
                (self.gameboard[0][1] == 1 and self.gameboard[1][1] == 1 and self.gameboard[2][1] == 1) or
                (self.gameboard[0][2] == 1 and self.gameboard[1][2] == 1 and self.gameboard[2][2] == 1)
            # Check if the minor or major diagonal has three 2's
            or (self.gameboard[0][0] == 1 and self.gameboard[1][1] == 1 and self.gameboard[2][2] == 1) or
                (self.gameboard[0][2] == 1 and self.gameboard[1][1] == 1 and self.gameboard[2][0] == 1)):
            stateObj['state'] = True
            stateObj['playerWon'] = "Player" if self.playerMark == 1 else 'CPU'

        # for 2
        # Check if one of the three rows have three 2's
        elif ((self.gameboard[0][0] == 2 and self.gameboard[0][1] == 2 and self.gameboard[0][2] == 2 or
               (self.gameboard[1][0] == 2 and self.gameboard[1][1] == 2 and self.gameboard[1][2] == 2) or
               (self.gameboard[2][0] == 2 and self.gameboard[2][1] == 2 and self.gameboard[2][2] == 2)
            # Check if one of the three columns have three 2's
            or (self.gameboard[0][0] == 2 and self.gameboard[1][0] == 2 and self.gameboard[2][0] == 2) or
               (self.gameboard[0][1] == 2 and self.gameboard[1][1] == 2 and self.gameboard[2][1] == 2) or
               (self.gameboard[0][2] == 2 and self.gameboard[1][2] == 2 and self.gameboard[2][2] == 2)
            # Check if the minor or major diagonal has three 2's
            or (self.gameboard[0][0] == 2 and self.gameboard[1][1] == 2 and self.gameboard[2][2] == 2) or
               (self.gameboard[0][2] == 2 and self.gameboard[1][1] == 2 and self.gameboard[2][0] == 2))):
            stateObj['state'] = True
            stateObj['playerWon'] = "Player" if self.playerMark == 2 else 'CPU'

        return stateObj

    def newGame(self):
        self.turns = 0

        # Randomize the player who goes first
        if (random.randint(0, 1) == 0):
            self.playerTurn = 'Your Turn'
        else:
            self.playerTurn = 'CPU'

        # Randomize the player who goes first
        if (random.randint(0, 1) == 0):
            self.playerMark = 1
            self.cpuMark = 2
        else:
            self.playerMark = 2
            self.cpuMark = 1

        # Reset the board
        self.gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def main():
    game = TicTacToe()


if __name__ == '__main__':
    main()

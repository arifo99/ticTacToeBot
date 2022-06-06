import pygame
from button import Button
from menu import Menu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Board:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.paused = False
        continueButton = Button("Continue", 100, 100, self.togglePaused)
        restartButton = Button("Restart", 100, 300, self.clearBoardAndTogglePaused)
        self.pauseMenu = Menu("Pause", [continueButton, restartButton])

    def clearBoard(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        
    def togglePaused(self):
        self.paused = not self.paused

    def clearBoardAndTogglePaused(self):
        self.clearBoard()
        self.togglePaused()

    def draw(self, screen):
        if not self.paused:
            square_length = int(self.SCREEN_HEIGHT/3)
            pygame.draw.line(screen, BLACK, (0, square_length), (self.SCREEN_WIDTH, square_length))
            pygame.draw.line(screen, BLACK, (0, 2*square_length), (self.SCREEN_WIDTH, 2*square_length))
            pygame.draw.line(screen, BLACK, (square_length, 0), (square_length, self.SCREEN_HEIGHT))
            pygame.draw.line(screen, BLACK, (2*square_length, 0), (2*square_length, self.SCREEN_HEIGHT))
            for row in range(3):
                for col in range(3):
                    if(self.board[row][col] == "X"):
                        pygame.draw.line(screen, BLACK, (square_length*row, square_length*col), (square_length*(row + 1), square_length*(col + 1)))
                        pygame.draw.line(screen, BLACK, (square_length*row, square_length*(col + 1)), (square_length*(row + 1), square_length*col))
                    elif(self.board[row][col] == "O"):
                        pygame.draw.circle(screen, BLACK, (square_length*row + int(square_length/2), square_length*col + int(square_length/2)), square_length/2)
                        pygame.draw.circle(screen, WHITE, (square_length*row + int(square_length/2), square_length*col + int(square_length/2)), square_length/2 - square_length/50)
        else:
            self.pauseMenu.draw(screen)

    def won(self):
        for i in range(3):
            if(self.board[i][0] != "" and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]):
                return True
            if(self.board[0][i] != "" and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]):
                return True

        if(self.board[0][0] != "" and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
            return True

        if(self.board[0][2] != "" and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
            return True

        return False

    def winner(self):
        if not self.won():
            return None
        
        for i in range(3):
            if(self.board[i][0] != "" and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]):
                return self.board[i][0]
            if(self.board[0][i] != "" and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        if(self.board[0][0] != "" and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
            return self.board[0][0]

        if(self.board[0][2] != "" and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
            return self.board[0][2]

    def stalemate(self):
        if(self.won()):
            return False

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False

        return True

    def whoseTurn(self):
        ct = 9
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    ct -= 1

        if(ct%2 == 0):
            return "X"
        return "O"

    def freeSquares(self):
        ct = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    ct += 1

        return ct

    def findDifference(self, otherBoard):
        for i in range(3):
            for j in range(3):
                if  self.board[i][j] != otherBoard.board[i][j]:
                    return (i, j)

        return None
            
    def update(self, clicked = False, escPressed = False):
        if escPressed:
            self.togglePaused()
        elif not self.paused and clicked:
            square_length = int(self.SCREEN_HEIGHT/3)
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseRow, mouseCol = int(mouseX/square_length), int(mouseY/square_length)
            if self.board[mouseRow][mouseCol] != "":
                return
            
            turn = 0
            for row in range(3):
                for col in range(3):
                    if(self.board[row][col] != ""):
                        turn = (turn + 1) % 2
                        
            if(turn == 0):
                self.board[mouseRow][mouseCol] = "X"
            else:
                self.board[mouseRow][mouseCol] = "O"

        if self.paused:
            self.pauseMenu.update(clicked)

import pygame
import tictacbot
from board import Board
from menu import Menu
from button import Button

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
activeScreen = "mainMenu"
difficulty = "easy"

def mainMenuPlayButtonClicked():
    global activeScreen
    activeScreen = "playMenu"
    
mainMenuPlayButton = Button("Play", 100, 100, mainMenuPlayButtonClicked)
mainMenu = Menu("Menu", [mainMenuPlayButton])

def playMenuPlayVsHumanClicked():
    global activeScreen
    activeScreen = "game"

def playMenuPlayVsBotClicked():
    global activeScreen
    activeScreen = "botDifficultyMenu"

def playMenuBackClicked():
    global activeScreen
    activeScreen="mainMenu"

def easyDifficultyClicked():
    global activeScreen, difficulty
    difficulty = "easy"
    activeScreen = "botGame"

def hardDifficultyClicked():
    global activeScreen, difficulty
    difficulty = "hard"
    activeScreen = "botGame"

playMenuPlayVsHumanButton = Button("Vs Human", 100, 100, playMenuPlayVsHumanClicked, width = 300)
playMenuPlayVsBotButton = Button("Vs Bot", 100, 250, playMenuPlayVsBotClicked)
playMenuBackButton = Button("Back", 100, 400, playMenuBackClicked)
playMenu = Menu("Play!", [playMenuPlayVsHumanButton, playMenuPlayVsBotButton, playMenuBackButton])

botDifficultyMenu = Menu("Difficulty", [Button("Easy", 100, 100, easyDifficultyClicked), Button("Hard", 100, 250, hardDifficultyClicked)])

xWonMenu = Menu("X Won!", [Button("Menu", 100, 400, playMenuBackClicked)])
oWonMenu = Menu("O Won!", [Button("Menu", 100, 400, playMenuBackClicked)])
drawMenu = Menu("Draw!", [Button("Menu", 100, 400, playMenuBackClicked)])

board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)

nextMove = tictacbot.getNextMove(board, "hard")

def start_game():
    global activeScreen
    playing = True
    
    while playing:
        screen.fill(WHITE)
        
        clicked = False
        escPressed = False
        
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                clicked = True

            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                   escPressed = True
                
        if activeScreen == "mainMenu":
            mainMenu.draw(screen)
            mainMenu.update(clicked)
            
        elif activeScreen == "playMenu":
            playMenu.draw(screen)
            playMenu.update(clicked)

        elif activeScreen == "botDifficultyMenu":
            botDifficultyMenu.draw(screen)
            botDifficultyMenu.update(clicked)

        elif activeScreen == "xWonMenu":
            xWonMenu.draw(screen)
            xWonMenu.update(clicked)
            
        elif activeScreen == "oWonMenu":
            oWonMenu.draw(screen)
            oWonMenu.update(clicked)

        elif activeScreen == "drawMenu":
            drawMenu.draw(screen)
            drawMenu.update(clicked)
            
        else:
            if board.whoseTurn() == "O" and activeScreen == 'botGame':
                nextMove = tictacbot.getNextMove(board, difficulty)
                board.board[nextMove[0]][nextMove[1]] = 'O'
                
            board.draw(screen)
            board.update(clicked = clicked, escPressed = escPressed)
            if(board.won()):
                activeScreen = board.winner().lower()+"WonMenu"
                board.clearBoard()
            elif(board.stalemate()):
                activeScreen = "drawMenu"
                board.clearBoard()

            
        pygame.display.update()

if __name__ == "__main__":
    start_game()

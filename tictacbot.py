import random
import json
import numpy as np

from board import Board

memoizedBoards={}
def getRotations(board):
    ans = [json.dumps(board)]
    boardNp = np.array(board)
    for i in range(3):
        np.rot90(boardNp)
        ans.append(json.dumps(boardNp.tolist()))
    return ans

def startMinMax(board):
    if board.won():
        score = board.freeSquares() + 1
        if board.whoseTurn() == 'O':
            return score*(-1), None
        return score, None
    
    elif board.stalemate():
        return 0, None

    score = -1000
    if board.whoseTurn() == 'X':
        score = 1000
        
    ansNextBoard = board
    nextBoards = []
    
    for i in range(3):
        for j in range(3):
            if board.board[i][j] != "":
                continue

            nextBoard = Board(board.SCREEN_WIDTH, board.SCREEN_HEIGHT)
            nextBoard.board = json.loads(json.dumps(board.board))
            nextBoard.board[i][j] = nextBoard.whoseTurn()
            nextBoardKey = json.dumps(nextBoard.board)
            
            if(memoizedBoards.get(nextBoardKey) is None):
                rotations = getRotations(nextBoard.board)
                miniMaxVal = startMinMax(nextBoard)[0]
                for rotationKey in rotations:
                    memoizedBoards[rotationKey] = miniMaxVal
                    
            nextScore = memoizedBoards[nextBoardKey]
            
            if board.whoseTurn() == 'X':
                if score >= nextScore:
                    score = nextScore
                    ansNextBoard = nextBoard
            else:
                if score <= nextScore:
                    score = nextScore
                    ansNextBoard = nextBoard
     
    return score, ansNextBoard
                
def getNextMove(board, difficulty):
    if difficulty == "easy":
        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if board.board[x][y] == "":
                return (x, y)
    else:
        ans = startMinMax(board)[1].findDifference(board)
        return ans

import numpy as np
from MainGameMath import BattleshipAI, SHIPLENGTH, BOARDSQUARES, NSHIPS
from Graph import plot



BOARDSIZE = BOARDSQUARES
GHOSTBOARDSIZE = BOARDSIZE + 2
SHIPSIZE = SHIPLENGTH


GhostArray = [[0 for y in range(GHOSTBOARDSIZE)]for x in range(GHOSTBOARDSIZE)]
for x in range(GHOSTBOARDSIZE - 2 ):
    for y in range(GHOSTBOARDSIZE - 2):
        GhostArray[x+1][y+1] = 1
        
shotBoard = np.array([[0 for y in range(BOARDSIZE)]for x in range(BOARDSIZE)])


def distfromZerox(x,y, board):
    #find index of our tile, if there is a zero on it's row, find it's index
    array = np.array(board)
    indices = np.where(array[x] == 0)[0] 
    distance = y-indices
    return distance

def distfromZeroy(x,y, board):
    #find index of our tile, if there is a zero on it's row, find it's index
    array = np.array(board)
    array = np.rot90(array,1)
    indices = np.where(array[x] == 0)[0] 
    distance = y-indices
    return distance

def gapSize(distance):
    if 0 in distance:
        return 0
    else:
        upDist = distance[(distance < SHIPSIZE) | (distance > -SHIPSIZE)]
        posValue = np.amin(upDist[upDist > 0])
        negValue = np.max(upDist[upDist < 0])
        if posValue is None:
            posValue = SHIPSIZE + 1
        if negValue is None:
            negValue = SHIPSIZE + 1
        return abs(posValue - negValue)

def smallestDistance(distance):
    return np.amin(abs(distance))

def numOfPoss(gap, sd):
    if gap <= SHIPSIZE:
        return 0
    elif gap >= SHIPSIZE*2:
        if sd < SHIPSIZE:
            return sd
        else:
            return SHIPSIZE
    elif gap == SHIPSIZE + 1:
        return 1
    else:
        return sd



def TiletoPossx(x,y,board):
    return numOfPoss(gapSize(distfromZerox(x,y,board)),smallestDistance(distfromZerox(x,y,board)))

def TiletoPossy(x,y,board):
    #board = np.rot90(board, 1)
    return numOfPoss(gapSize(distfromZeroy(x,y,board)),smallestDistance(distfromZeroy(x,y,board)))



def createPossArrayx(board): # creates a 2D which represents the number possible ship placements in each board square
    array = [[0 for i in range(BOARDSIZE+2)] for j in range(BOARDSIZE+2)]
    for x in range(BOARDSIZE+2):
        for y in range(BOARDSIZE+2):
            array[x][y] = TiletoPossx(x,y,board)
            array = np.array(array)
    return array[1:BOARDSIZE+1, 1:BOARDSIZE+1]

def createPossArrayy(board):
    arrayy = [[0 for i in range(BOARDSIZE+2)] for j in range(BOARDSIZE+2)]
    for x in range(BOARDSIZE+2):
        for y in range(BOARDSIZE+2):
            arrayy[x][y] = TiletoPossy(x,y,board)
            arrayy = np.array(arrayy)
    arrayy = np.rot90(arrayy,-1)
    return arrayy[1:BOARDSIZE+1, 1:BOARDSIZE+1]
    

def createCombinedArray(board):
    return createPossArrayx(board) + createPossArrayy(board)


def updateShotArray(x,y,board):
    board[x][y] = 2
    return board


def shotlogic(board):
    noOfHits = np.where(shotBoard==2)
    if len(noOfHits[0]) > 1:
        for x in range(SHIPLENGTH-2):
            hit1x = int(noOfHits[0][x])
            hit1y = int(noOfHits[1][x])
            nextshot = [hit1x+1,hit1y]
            if nextshot[0] >= len(board):
                nextshot = [hit1x,hit1y]
                pass
            elif board[hit1x][hit1y] == board[hit1x+1][hit1y]:
                nextshot = [hit1x+2,hit1y]
                if nextshot[0] >= len(board):
                    nextshot = [hit1x-1, hit1y]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [hit1x-1,hit1y]
                    if hit1x-1 < 0:
                        nextshot = [hit1x,hit1y]
                        pass
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    pass
            if board[hit1x][hit1y] == board[hit1x-1][hit1y]:
                nextshot = [hit1x-2,hit1y]
                if hit1x-2 < 0:
                    nextshot = [hit1x,hit1y]
                    pass
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [hit1x+1,hit1y]
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    pass
            nextshot = [hit1x,hit1y+1]
            if nextshot[1] >= len(board):
                nextshot = [hit1x,hit1y]
                pass
            elif board[hit1x][hit1y] == board[hit1x][hit1y+1]:
                nextshot = [hit1x,hit1y+2]
                if nextshot[1] >= len(board):
                    nextshot = [hit1x, hit1y-1]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [hit1x,hit1y-1]
                    if hit1y-1 < 0:
                        nextshot = [hit1x,hit1y]
                        pass
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    pass
            if board[hit1x][hit1y] == board[hit1x][hit1y-1]:
                nextshot = [hit1x,hit1y+1]
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [hit1x,hit1y-2]
                    if hit1y-2 < 0:
                        nextshot = [hit1x,hit1y]
                        pass
                if board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    pass
    else:
        if 2 in board:
            lent = np.where(board==2)
            lenth = len(lent[0])
            for x in range(lenth):
                hitcord = np.where(board==2)
                nextshotx = int(hitcord[0][x])
                nextshoty = int(hitcord[1][x])
                nextshot = [nextshotx+1,nextshoty]
                if nextshot[0] >= len(board):
                    nextshot = [nextshotx-1, nextshoty]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [nextshotx-1, nextshoty]
                if nextshot[0] < 0:
                    nextshot = [nextshotx, nextshoty+1]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [nextshotx, nextshoty+1]
                if nextshot[1] >= len(board):
                    nextshot = [nextshotx, nextshoty-1]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    nextshot = [nextshotx, nextshoty-1]
                if nextshot[1] < 0:
                    nextshot = [nextshotx,nextshoty]
                    pass
                elif board[nextshot[0]][nextshot[1]] == 0:
                    return nextshot
                else:
                    pass
    

        else:
            maxprob = np.amax(createCombinedArray(GhostArray))
            maxprobloc = np.where(createCombinedArray(GhostArray)==maxprob)
            maxproby = int(maxprobloc[0][0])
            maxprobx = int(maxprobloc[1][0])
            nextshot = [maxproby,maxprobx]
            return nextshot


def updateGhostBoard(shot):
    GhostArray[shot[0]+1][shot[1]+1] = 0

def updateShotBoard(shot, hit):
    global shotBoard
    if hit == True:
        shotBoard[shot[0]][shot[1]] = 2
    else:
        shotBoard[shot[0]][shot[1]] = 1

def updateShotBoardOld(shot):
    shotBoard[shot[0]][shot[1]] = 1
    
def resetBoards():
    global GhostArray, shotBoard
    GhostArray = [[0 for y in range(GHOSTBOARDSIZE)]for x in range(GHOSTBOARDSIZE)]
    for x in range(GHOSTBOARDSIZE - 2 ):
        for y in range(GHOSTBOARDSIZE - 2):
            GhostArray[x+1][y+1] = 1
            
    shotBoard = np.array([[0 for y in range(BOARDSIZE)]for x in range(BOARDSIZE)])

def solver():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 9
    game = BattleshipAI()
    games = 1
    hit = False
    
    while True:
        combarray = createCombinedArray(GhostArray)
        shot = shotlogic(shotBoard)
        reward, done, score, hit = game.Gamer(shot)
        updateGhostBoard(shot)
        updateShotBoard(shot, hit)
        if done:
            game.reset()
            resetBoards()


            if score < record:
                record = score

            print('Game', games, 'Score', score, 'Record:', record)
            games += 1

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
   solver()
from distutils.ccompiler import get_default_compiler
import numpy as np
import matplotlib.pyplot as plt


BOARDSIZE = 8
GHOSTBOARDSIZE = BOARDSIZE + 2
SHIPSIZE = 4


def CreateGBoard():
    global GhostArrayx, GhostArrayy
    GhostArray = [[0 for y in range(GHOSTBOARDSIZE)]for x in range(GHOSTBOARDSIZE)]

    for x in range(GHOSTBOARDSIZE - 2 ):
        for y in range(GHOSTBOARDSIZE - 2):
            GhostArray[x+1][y+1] = 1
    GhostArrayx = GhostArray


def distfromZerox(x,y, board):
    #find index of our tile, if there is a zero on it's row, find it's index
    array = np.array(board)
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



def TiletoPoss(x,y,board):
    return numOfPoss(gapSize(distfromZerox(x,y,board)),smallestDistance(distfromZerox(x,y,board)))


def createPossArray(board): # creates a 2D which represents the number possible ship placements in each board square
    array = [[0 for i in range(BOARDSIZE+2)] for j in range(BOARDSIZE+2)]
    for x in range(BOARDSIZE+2):
        for y in range(BOARDSIZE+2):
            array[x][y] = TiletoPoss(x,y,board)
            array = np.array(array)
    return array[1:BOARDSIZE+1, 1:BOARDSIZE+1]

def createPossArrayy(board):
    array = np.rot90(board, 1)
    return array

labels = []
for x in range(BOARDSIZE):
    labels.append(x)



testBoard = [[1,1,1,1,1,1,1],[1,1,0,1,0,1,0],[0,0,0,1,1,0,0],[0,0,0,1,1,1,1],[1,1,0,1,1,0,1]]
testGhostArray = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 
1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 
1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])  
testGhostArrayy = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 
1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 
1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])



CreateGBoard()
print(createPossArray(GhostArrayx) + createPossArrayy(createPossArray(GhostArrayx)))
#print(testGhostArray)




#TODO TOMMORROW
# - CREATE A NEW 2D BLANK ARRAY THAT TRACKS EVERY SHOT
# - 
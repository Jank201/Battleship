BOARDSIZE = 8
SHIPSIZE = 3


def distanceFromEdge(x,y): #this function finds how far away any given coordinate is from the edges of the board
    distx = int(-abs(x- (BOARDSIZE/2) + 1/2) + (BOARDSIZE/2 - 1/2))
    disty = int(-abs(y- (BOARDSIZE/2) + 1/2) + (BOARDSIZE/2 - 1/2))
    return distx, disty

def numOfPoss(x,y): #finds how many possible placements of ships would exist in the square given how far away it is from the edges
    if x < (SHIPSIZE-1):
        if y < (SHIPSIZE-1):
            num = 2+x+y
        else:
            num = 2 + x + (SHIPSIZE-1)
    else:
        if y < (SHIPSIZE-1):
            num = 2 + (SHIPSIZE-1) + y
        else:
            num = 2 + 2*(SHIPSIZE-1)
    return num

def createPossArray(): # creates a 2D which represents the number possible ship placements in each board square
    array = [[0 for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
    for x in range(BOARDSIZE):
        for y in range(BOARDSIZE):
            x1, y1 = distanceFromEdge(x,y)
            array[x][y] = numOfPoss(x1,y1)
    return array
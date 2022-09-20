from random import randint

shipBoard = [[' ']*8 for x in range(8)]
GuessBoard = [[' ']*8 for x in range(8)]

letters = ['A','B','C','D','E','F','G','H']
letterToNumber = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G': 6, 'H': 7}

def createBoard(board):
    print('  A B C D E F G H')
    print('  _______________')
    rowNo = 1
    for row in board:
        print("%d|%s|"% (rowNo, '|'.join(row)))
        rowNo+= 1


possibleCoordinates = []

for letter in range(8):
    for number in range(1,9):
        coordinate = letters[letter] + str(number)
        possibleCoordinates.append(coordinate)

def Ships(board):
    shipLocation = [0,0,0]
    shipOrigins = [[]]
    shipOrigin = []
    direction = randint(0,1) # randomly decides whether ship is horiztonal or vertical
    shipLocation[2] = direction
    if direction == 0: # ship is horizontal
        shipOriginx = randint(0,4)
        shipOriginy = randint(0,7)
        for x in range(3):
            board[shipOriginx+x][shipOriginy] = 'X'
    else: #ship is vertical
        shipOriginx = randint(0,7)
        shipOriginy = randint(0,4)
        for y in range(3):
            board[shipOriginx][shipOriginy+y] = 'X'
    shipLocation[0], shipLocation[1] = shipOriginx, shipOriginy
    return shipLocation

def aim():
    target = [0,0]
    command = input('Please Enter Coordinates: ')
    if command.upper() not in possibleCoordinates:
        command = input('Please Enter a Valid Coordinate(A1-H8): ')
    targetRaw = list(command)
    column = letterToNumber[targetRaw[0].upper()]
    row = int(targetRaw[1]) - 1
    target[1], target[0] = column, row
    return target


def hitOrNo(target, shipLocation):
    global Shots
    global Hits
    if shipLocation[2] == 0:
        if (shipLocation[0] == target[0] or shipLocation[0] + 1 == target[0] or shipLocation[0] + 2 == target[0]) and shipLocation[1]== target[1]:
            print('HIT!')
            GuessBoard[target[0]][target[1]] = 'X'
            Hits += 1
            Shots += 1
        else:
            print('Miss')
            GuessBoard[target[0]][target[1]] = '-'
            Shots += 1
            
    elif shipLocation[2] == 1:
        if (shipLocation[1] == target[1] or shipLocation[1] + 1 == target[1] or shipLocation[1] + 2 == target[1]) and shipLocation[0]== target[0]:
            print('HIT!')
            GuessBoard[target[0]][target[1]] = 'X'
            Hits += 1
            Shots += 1
        else:
            print('Miss')
            GuessBoard[target[0]][target[1]] = '-'
            Shots += 1
    return True 





shipPlacement = Ships(shipBoard)
createBoard(shipBoard)
Shots = 0
Hits = 0
while Hits < 3:
    target = aim()
    Success = hitOrNo(target, shipPlacement)
    createBoard(GuessBoard)
print('You Sunk the Ship!')
print('Game Over')
print('You completed the game in '+str(Shots)+' Shots')









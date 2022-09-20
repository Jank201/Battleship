import pygame
from random import randint 
import time
import numpy as np

BOARDSQUARES = 3
SHIPLENGTH = 3


FPS = 100
H = 600
W = 800
TILESIZE = 400/BOARDSQUARES
BOARDDIM = 10
TEXTSIZE = 40



XMARGIN = 30 #x-position of the top left corner of board 
YMARGIN = 30 #y-position of the top left corner of board


BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,204,0)
GRAY = (60,60,60)
BLUE = (0,50,255)
YELLOW = (255,255,0)
DARKGRAY = (40,40,40)
LIGHTBLUE = (77,118,184)


SHIPCOLOUR = GRAY
TILECOLOUR = BLUE
BGCOLOUR = LIGHTBLUE

pygame.init()
pygame.display.set_caption('BattleshipAI')

class BattleshipAI:

    def __init__(self, w = W, h = H):
        self.w = w
        self.h = h
        global DISPLAYSURF
        DISPLAYSURF = pygame.display.set_mode((self.w,self.h))
        DISPLAYSURF.fill(BGCOLOUR)
        self.clock = pygame.time.Clock()
        self.reset()
            
    def Gamer(self, action):
        self.gameOver = False
        self.frameIteration += 1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        self.reward = 0
        self.getTilefromInput(action)
        self._draw_board(self.shipBoard)
        pygame.display.update()
        if self.shipTiles == 0:
            self.gameOver = True
    
        self.clock.tick(FPS)

        return self.reward, self.gameOver, self.shots


    def reset(self):
        time.sleep(0.1)
        self.shots = 0
        self.shipTiles = 3
        self.upBoard = self._createBoard()
        self._draw_board(self.upBoard)
        self.frameIteration = 0


    def _createBoard(self):
        direction = randint(0,1)
        self.shipBoard = [[[0] for i in range(BOARDSQUARES)] for y in range(BOARDSQUARES)]
        if direction == 0:
            originx = 0
            originy = randint(0,BOARDSQUARES-1)
            for x in range(SHIPLENGTH):
                    self.shipBoard[originx+x][originy] = 1
            return self.shipBoard
        else:
            originx = randint(0,BOARDSQUARES-1)
            originy = 0
            for y in range(SHIPLENGTH):
                    self.shipBoard[originx][originy+y] = 1
            return self.shipBoard

    def _drawWindow(self):
        DISPLAYSURF.fill(LIGHTBLUE)


    def _draw_board(self,board):
        
        for x in range(BOARDSQUARES):
            for y in range(BOARDSQUARES):
                if board[x][y] == 1:
                    pygame.draw.rect(DISPLAYSURF, GRAY, (XMARGIN+(TILESIZE+10)*x,YMARGIN+(TILESIZE+10)*y, TILESIZE, TILESIZE))
                elif board[x][y] == 3:
                    pygame.draw.rect(DISPLAYSURF, YELLOW, (XMARGIN+(TILESIZE+10)*x,YMARGIN+(TILESIZE+10)*y, TILESIZE, TILESIZE))
                elif board[x][y] == 4:
                    pygame.draw.rect(DISPLAYSURF, RED, (XMARGIN+(TILESIZE+10)*x,YMARGIN+(TILESIZE+10)*y, TILESIZE, TILESIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, BLUE, (XMARGIN+(TILESIZE+10)*x,YMARGIN+(TILESIZE+10)*y, TILESIZE, TILESIZE))
        pygame.display.update()

    def _getPixelofTile(self,tilex,tiley):
        left = tilex*(TILESIZE+10) + XMARGIN
        top = tiley*(TILESIZE+10) + YMARGIN
        return (left,top)

    def _getTileofPixel(self,x,y):
        for tilex in range(BOARDSQUARES):
            for tiley in range(BOARDSQUARES):
                left,top = self._getPixelofTile(tilex,tiley)
                tileRect = pygame.Rect(left,top,TILESIZE,TILESIZE)
                if tileRect.collidepoint(x,y):
                    return (tilex,tiley)
        return (None,None)

    def getTilefromInput(self, action):
        if np.array_equal(action, [1,0,0,0,0,0,0,0,0]):
            if self.shipBoard[0][2] == 1:
                self.shipTiles -= 1
                self.shipBoard[0][2] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[0][2] == 3:
                self.reward = -10
            elif self.shipBoard[0][2] == 4:
                self.reward = -10
                self.shipBoard[0][2] = 4
            else:
                self.shots += 1
                self.shipBoard[0][2] = 3
                self.reward = -10
        if np.array_equal(action, [0,1,0,0,0,0,0,0,0]):
            if self.shipBoard[1][2] == 1:
                self.shipTiles -= 1
                self.shipBoard[1][2] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[1][2] == 3:
                self.reward = -10
            elif self.shipBoard[1][2] == 4:
                self.reward = -10
                self.shipBoard[1][2] = 4
            else:
                self.shots += 1
                self.shipBoard[1][2] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,1,0,0,0,0,0,0]):
            if self.shipBoard[2][2] == 1:
                self.shipTiles -= 1
                self.shipBoard[2][2] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[2][2] == 3:
                self.reward = -10
            elif self.shipBoard[2][2] == 4:
                self.reward = -10
                self.shipBoard[2][2] = 4
            else:
                self.shots += 1
                self.shipBoard[2][2] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,1,0,0,0,0,0]):
            if self.shipBoard[0][1] == 1:
                self.shipTiles -= 1
                self.shipBoard[0][1] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[0][1] == 3:
                self.reward = -10
            elif self.shipBoard[0][1] == 4:
                self.reward = -10
                self.shipBoard[0][1] = 4
            else:
                self.shots += 1
                self.shipBoard[0][1] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,0,1,0,0,0,0]):
            if self.shipBoard[1][1] == 1:
                self.shipTiles -= 1
                self.shipBoard[1][1] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[1][1] == 3:
                self.reward = -10
            elif self.shipBoard[1][1] == 4:
                self.shipBoard[1][1] = 4
                self.reward = -10
            else:
                self.shots += 1
                self.shipBoard[1][1] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,0,0,1,0,0,0]):
            if self.shipBoard[2][1] == 1:
                self.shipTiles -= 1
                self.shipBoard[2][1] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[2][1] == 3:
                self.reward = -10
            elif self.shipBoard[2][1] == 4:
                self.reward = -10
                self.shipBoard[2][1] = 4
            else:
                self.shots += 1
                self.shipBoard[2][1] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,0,0,0,1,0,0]):
            if self.shipBoard[0][0] == 1:
                self.shipTiles -= 1
                self.shipBoard[0][0] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[0][0] == 3:
                self.reward = -10
            elif self.shipBoard[0][0] == 4:
                self.reward = -10
                self.shipBoard[0][0] = 4
            else:
                self.shots += 1
                self.shipBoard[0][0] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,0,0,0,0,1,0]):
            if self.shipBoard[1][0] == 1:
                self.shipTiles -= 1
                self.shipBoard[1][0] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[1][0] == 3:
                self.reward = -10
            elif self.shipBoard[1][0] == 4:
                self.shipBoard[1][0] = 4
                self.reward = -10
            else:
                self.shots += 1
                self.shipBoard[1][0] = 3
                self.reward = -10
        if np.array_equal(action, [0,0,0,0,0,0,0,0,1]):
            if self.shipBoard[2][0] == 1:
                self.shipTiles -= 1
                self.shipBoard[2][0] = 4
                self.shots += 1
                self.reward = 10
            elif self.shipBoard[2][0] == 3:
                self.reward = -10
            elif self.shipBoard[2][0] == 4:
                self.shipBoard[2][0] = 4
                self.reward = -10
            else:
                self.shots += 1
                self.shipBoard[2][0] = 3
                self.reward = -10



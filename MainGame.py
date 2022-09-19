import numbers
from xml.etree.ElementTree import TreeBuilder
import pygame
from random import randint 
import time

FPS = 60
TILESIZE = 50
BOARDDIM = 100
BOARDSQUARES = 3
TEXTSIZE = 40
SHIPLENGTH = 3


XMARGIN = int((600 - (BOARDSQUARES * TILESIZE) - BOARDDIM - TEXTSIZE) / 2) #x-position of the top left corner of board 
YMARGIN = int((800 - (BOARDSQUARES * TILESIZE) - TEXTSIZE) / 2) #y-position of the top left corner of board

BLACK   = (  0,   0,   0)
RED     = (255,0,0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 204,   0)
GRAY    = ( 60,  60,  60)
BLUE    = (  0,  50, 255)
YELLOW  = (255, 255,   0)
DARKGRAY =( 40,  40,  40)
LIGHTBLUE = (77,118,184)


SHIPCOLOUR = GRAY
TILECOLOUR = BLUE
BGCOLOUR = LIGHTBLUE

pygame.init()
pygame.display.set_caption('Battleship')

class BattleShip:
    def __init__(self, w = 600, h = 800):
        self.w = w
        self.h = h
        global DISPLAYSURF
        DISPLAYSURF = pygame.display.set_mode((self.w,self.h))
        DISPLAYSURF.fill(BGCOLOUR)
        self.clock = pygame.time.Clock()
        self.reset()
            
    def Gamer(self):
        self.gameOver = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
        self._getTilefromInput()
        self._draw_board(self.shipBoard)
        pygame.display.update()
        if self.shipTiles == 0:
            self.gameOver = True
    

        self.clock.tick(FPS)

        return self.gameOver, self.shots


        
    
        


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



    def _draw_board(self,board):
        
        for x in range(BOARDSQUARES):
            for y in range(BOARDSQUARES):
                if board[x][y] == 1:
                    pygame.draw.rect(DISPLAYSURF, GRAY, (XMARGIN+60*x,YMARGIN+60*y, TILESIZE, TILESIZE))
                elif board[x][y] == 3:
                    pygame.draw.rect(DISPLAYSURF, YELLOW, (XMARGIN+60*x,YMARGIN+60*y, TILESIZE, TILESIZE))
                elif board[x][y] == 4:
                    pygame.draw.rect(DISPLAYSURF, RED, (XMARGIN+60*x,YMARGIN+60*y, TILESIZE, TILESIZE))
                else:
                    pygame.draw.rect(DISPLAYSURF, BLUE, (XMARGIN+60*x,YMARGIN+60*y, TILESIZE, TILESIZE))
        pygame.display.update()

    def reset(self):
        time.sleep(1)
        self.shots = 0
        self.shipTiles = 3
        self.upBoard = self._createBoard()
        self._draw_board(self.upBoard)
        self.frameIteration = 0
        



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

    def _getTilefromInput(self):
        self.shipBoard = self.upBoard
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_KP1]:
            if self.shipBoard[0][2] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[0][2] = 4
                self.shots += 1
            elif self.shipBoard[0][2] == 3:
                print('you already shot here')
            elif self.shipBoard[0][2] == 4:
                print('you already shot here')
                self.shipBoard[0][2] = 4
            else:
                self.shots += 1
                self.shipBoard[0][2] = 3
                print('miss')
        if key_pressed[pygame.K_KP2]:
            if self.shipBoard[1][2] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[1][2] = 4
                self.shots += 1
            elif self.shipBoard[1][2] == 3:
                print('you already shot here')
            elif self.shipBoard[1][2] == 4:
                print('you already shot here')
                self.shipBoard[1][2] = 4
            else:
                self.shots += 1
                self.shipBoard[1][2] = 3
                print('miss')
        if key_pressed[pygame.K_KP3]:
            if self.shipBoard[2][2] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[2][2] = 4
                self.shots += 1
            elif self.shipBoard[2][2] == 3:
                print('you already shot here')
            elif self.shipBoard[2][2] == 4:
                print('you already shot here')
                self.shipBoard[2][2] = 4
            else:
                self.shots += 1
                self.shipBoard[2][2] = 3
                print('miss')
        if key_pressed[pygame.K_KP4]:
            if self.shipBoard[0][1] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[0][1] = 4
                self.shots += 1
            elif self.shipBoard[0][1] == 3:
                print('you already shot here')
            elif self.shipBoard[0][1] == 4:
                print('you already shot here')
                self.shipBoard[0][1] = 4
            else:
                self.shots += 1
                self.shipBoard[0][1] = 3
                print('miss')
        if key_pressed[pygame.K_KP5]:
            if self.shipBoard[1][1] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[1][1] = 4
                self.shots += 1
            elif self.shipBoard[1][1] == 3:
                print('you already shot here')
            elif self.shipBoard[1][1] == 4:
                print('you already shot here')
                self.shipBoard[1][1] = 4
            else:
                self.shots += 1
                self.shipBoard[1][1] = 3
                print('miss')
        if key_pressed[pygame.K_KP6]:
            if self.shipBoard[2][1] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[2][1] = 4
                self.shots += 1
            elif self.shipBoard[2][1] == 3:
                print('you already shot here')
            elif self.shipBoard[2][1] == 4:
                print('you already shot here')
                self.shipBoard[2][1] = 4
            else:
                self.shots += 1
                self.shipBoard[2][1] = 3
                print('miss')
        if key_pressed[pygame.K_KP7]:
            if self.shipBoard[0][0] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[0][0] = 4
                self.shots += 1
            elif self.shipBoard[0][0] == 3:
                print('you already shot here')
            elif self.shipBoard[0][0] == 4:
                print('you already shot here')
                self.shipBoard[0][0] = 4
            else:
                self.shots += 1
                self.shipBoard[0][0] = 3
                print('miss')
        if key_pressed[pygame.K_KP8]:
            if self.shipBoard[1][0] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[1][0] = 4
                self.shots += 1
            elif self.shipBoard[1][0] == 3:
                print('you already shot here')
            elif self.shipBoard[1][0] == 4:
                print('you already shot here')
                self.shipBoard[1][0] = 4
            else:
                self.shots += 1
                self.shipBoard[1][0] = 3
                print('miss')
        if key_pressed[pygame.K_KP9]:
            if self.shipBoard[2][0] == 1:
                print('HIT')
                self.shipTiles -= 1
                self.shipBoard[2][0] = 4
                self.shots += 1
            elif self.shipBoard[2][0] == 3:
                print('you already shot here')
            elif self.shipBoard[2][0] == 4:
                print('you already shot here')
                self.shipBoard[2][0] = 4
            else:
                self.shots += 1
                self.shipBoard[2][0] = 3
                print('miss')
        pygame.display.update()


    




if __name__ == '__main__':
    game = BattleShip()
    while True:
        game_over, score = game.Gamer()

        if game_over == True:
            print('You won in', score, 'Shots')
            game.reset()




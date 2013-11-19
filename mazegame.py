import os, sys
import pygame
from board import Board

START = [['S','O','F',' ','O',' ','G'],
         [' ','O',' ',' ','O',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         ['O','O',' ',' ',' ','O','O'],
         [' ',' ',' ',' ',' ',' ','F'],
         ['F',' ',' ',' ',' ',' ','O']]

CELL_SIZE = 100
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
SCREEN_WIDTH = BOARD_WIDTH*CELL_SIZE
SCREEN_HEIGHT = BOARD_HEIGHT*CELL_SIZE
BG_COLOR = (255,255,255)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    board = Board(BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE)
    
    for j in range(BOARD_HEIGHT):
        for i in range(BOARD_WIDTH):
            if START[j][i] == 'S':
                board.addStart(i,j)
                board.addPlayer(i,j)
            elif START[j][i] == 'O':
                board.addObstacle(i,j)
            elif START[j][i] == 'F':
                board.addFlag(i,j)
            elif START[j][i] == 'G':
                board.addGoal(i,j)
    
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board.moveUp()
                elif event.key == pygame.K_DOWN:
                    board.moveDown()
                elif event.key == pygame.K_RIGHT:
                    board.moveRight()
                elif event.key == pygame.K_LEFT:
                    board.moveLeft()
                
        screen.fill(BG_COLOR)
        board.display(screen)
        
        pygame.display.flip()
        
if __name__ == '__main__':
    run_game()

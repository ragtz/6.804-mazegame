import pygame
from flag import Flag
from goal import Goal
from obstacle import Obstacle
from player import Player

class Obj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Board:
    def __init__(self, width, height, cell_size):
        self.w = width
        self.h = height
        self.cell_size = cell_size
        self.start = None
        self.goal = None
        self.player = None
        self.obstacles = []
        self.flags = []
        self.captured_flags = []
    
    def _valid(self, x, y):
        return x >= 0 and x < self.w and y >= 0 and y < self.h
        
    def _collide(self, x, y):
        return Obj(x,y) in self.obstacles
        
    def _checkFlags(self):
        if self.player in self.flags:
            self.flags.remove(self.player)
            self.captured_flags.append(Flag(self.player.x, self.player.y, self.cell_size/2))
    
    def _checkGoal(self):
        if self.player == self.goal:
            self.player.update(self.start[0], self.start[1])
            if self.flags == []:
                self.flags = list(self.captured_flags)
            else:
                self.flags.extend(self.captured_flags)
            self.captured_flags = []
    
    def addStart(self, x, y):
        if self._valid(x, y):
            self.start = (x, y)
    
    def addGoal(self, x, y):
        if self._valid(x, y):
            self.goal = Goal(x, y, self.cell_size)
        
    def addPlayer(self, x, y):
        if self._valid(x, y):
            self.player = Player(x, y, self.cell_size/2)
    
    def addObstacle(self, x, y):
        if self._valid(x, y):
            self.obstacles.append(Obstacle(x, y, self.cell_size))
    
    def addObstacles(self, obstacles):
        for (x,y) in obstacles:
            self.addObstacle(x, y)
    
    def addFlag(self, x, y):
        if self._valid(x, y):
            self.flags.append(Flag(x, y, self.cell_size/2))
    
    def addFlags(self, flags):
        for (x,y) in flags:
            self.addFlag(x, y)
            
    def moveUp(self):
        if self._valid(self.player.x,self.player.y-1) and not self._collide(self.player.x,self.player.y-1):
            self.player.update(self.player.x,self.player.y-1)
            
        self._checkFlags()
        self._checkGoal()
    
    def moveDown(self):
        if self._valid(self.player.x,self.player.y+1) and not self._collide(self.player.x,self.player.y+1):
            self.player.update(self.player.x,self.player.y+1)
            
        self._checkFlags()
        self._checkGoal()
    
    def moveRight(self):
        if self._valid(self.player.x+1,self.player.y) and not self._collide(self.player.x+1,self.player.y):
            self.player.update(self.player.x+1,self.player.y)
            
        self._checkFlags()
        self._checkGoal()
                
    def moveLeft(self):
        if self._valid(self.player.x-1,self.player.y) and not self._collide(self.player.x-1,self.player.y):
            self.player.update(self.player.x-1,self.player.y)
        
        self._checkFlags()
        self._checkGoal()
   
    def display(self, screen):
        self.player.display(screen)
        self.goal.display(screen)
        
        for flag in self.flags:
            flag.display(screen)
            
        for obstacle in self.obstacles:
            obstacle.display(screen)
        

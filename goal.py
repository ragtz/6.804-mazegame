import pygame

class Goal:
    def __init__(self, x, y, size, color = (0,255,0), width = 0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
    
    def display(self, screen):
        b_x = self.size*self.x
        b_y = self.size*self.y
        pygame.draw.rect(screen, self.color, pygame.Rect(b_x, b_y, self.size, self.size), self.width)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

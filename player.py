import pygame

class Player:
    def __init__(self, x, y, radius, color = (200,0,0), width = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = width
        
    def update(self, x, y):
        self.x = x
        self.y = y
    
    def display(self, screen):
        b_x = 2*self.radius*self.x + self.radius
        b_y = 2*self.radius*self.y + self.radius
        pygame.draw.circle(screen, self.color, (b_x, b_y), self.radius, self.width)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        

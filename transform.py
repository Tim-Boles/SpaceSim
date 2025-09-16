import pygame

class Transform(object):
    def __init__(self, position: pygame.Vector2):
        self.position = position
        self.direction: float = 0
        self.acceleration = pygame.Vector2(0,0)
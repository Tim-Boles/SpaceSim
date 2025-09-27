import pygame
import math
from typing import Any
from animation import Animation
from transform import Transform

class Actor(object):
    def __init__(self, name: str, actor_animation: Animation, actor_transform: Transform) -> None:
        self.name = name
        self.created = False
        self.animation = actor_animation
        self.transform = Transform(actor_transform.position.copy())
        self.transform.direction = actor_transform.direction
        self.transform.velocity = actor_transform.velocity.copy()
        self.is_off_screen = False
        self.destroy = False

    def start(self):
        self.animation.start()

    def update(self, dt, args: dict[str, Any]):
        self.animation.update(dt, self.transform, args["screen"])
        self.off_screen(args)

    def create(self, args: dict[str, Any]):
        """Create a new Actor
        
        Keyword arguments: \n
        args -- a dict containing the following values\n ["angle" : , "pos"]\n
        Return: None
        """
        
        self.created = True
        self.transform.direction = args["angle"]
        self.transform.position = args["pos"]
    
    def off_screen(self, args: dict[str, Any]):
        if self.transform.position.x > args["screen"].width + 1:
            self.is_off_screen = True
        elif self.transform.position.x < -1:
            self.is_off_screen = True
        elif self.transform.position.y > args["screen"].height + 1:
            self.is_off_screen = True
        elif self.transform.position.y < -1:
            self.is_off_screen = True
        else:
            self.is_off_screen = False

    def print(self):
        print(f"{self.name}self.transform.acceleration")
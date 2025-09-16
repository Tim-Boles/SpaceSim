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
        self.transform = actor_transform

    def start(self):
        self.animation.start()

    def update(self, dt, args: dict[str, Any]):
        self.animation.update(dt, self.transform, args["screen"])

    def create(self, args: dict[str, Any]):
        """Create a new Actor
        
        Keyword arguments: \n
        args -- a dict containing the following values\n ["angle" : , "pos"]\n
        Return: None
        """
        
        self.created = True
        self.transform.direction = args["angle"]
        self.transform.position = args["pos"]

    def print(self):
        print(f"{self.name}self.transform.acceleration")
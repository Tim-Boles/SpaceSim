import pygame
from actor import Actor
from animation import Animation
from transform import Transform

class Asteroid(Actor):
    def __init__(self, name: str, actor_animation: Animation, actor_transform: Transform) -> None:
        super().__init__(name, actor_animation, actor_transform)
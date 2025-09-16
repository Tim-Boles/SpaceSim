import math
import pygame
from actor import Actor
from animation import Animation
from transform import Transform

class Laser(Actor):
    def __init__(self, name: str, actor_animation: Animation, actor_transform: Transform, speed: int) -> None:
        self.speed = speed
        super().__init__(name, actor_animation, actor_transform)
    
    def start(self):
        return super().start()

    def update(self, dt, args):
        self.transform.position += self.transform.acceleration * self.speed * dt
        return super().update(dt, args)
    
    def create(self, args):
        self.transform.acceleration = pygame.Vector2(math.cos(args["angle"]), -math.sin(args["angle"]))
        args["pos"] = args["player_pos"]
        return super().create(args)
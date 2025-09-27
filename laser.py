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
        if self.is_off_screen:
            self.destroy = True
        self.transform.position += self.transform.velocity * dt
        return super().update(dt, args)
    
    def create(self, args):
        # 1. Get the laser's direction (a vector with length 1)
        laser_direction = pygame.Vector2(math.cos(args["angle"]), -math.sin(args["angle"]))

        # 2. Calculate the laser's own velocity (Muzzle Velocity)
        laser_muzzle_velocity = laser_direction * self.speed

        # 3. The final velocity is the muzzle velocity + the ship's velocity
        self.transform.velocity = laser_muzzle_velocity + args["player_velocity"]

        args["pos"] = args["player_pos"]

        return super().create(args)
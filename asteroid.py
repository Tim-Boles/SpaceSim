import pygame
import random
import math
from actor import Actor
from animation import Animation
from transform import Transform

class Asteroid(Actor):
    def __init__(self, name: str, actor_animation: Animation, actor_transform: Transform, speed: int) -> None:
        self.speed = speed
        self.has_hit_screen = False
        self.on_screen_counter = 0
        super().__init__(name, actor_animation, actor_transform)
    
    def start(self):
        return super().start()

    def update(self, dt, args):
        if self.is_off_screen and self.has_hit_screen:
            self.destroy = True
        if not self.is_off_screen:
            self.on_screen_counter += 1
            if self.on_screen_counter > 10:
                self.has_hit_screen = True
        self.transform.position += self.transform.velocity * dt
        return super().update(dt, args)
    
    def create(self, args):
        # 1. Get the asteroid's direction (a vector with length 1)
        asteroid_direction = pygame.Vector2(math.cos(args["angle"]), math.sin(args["angle"]))

        # 2. Calculate the asteroid's own velocity
        asteroid_velocity = asteroid_direction * self.speed

        # 3. The final velocity
        self.transform.velocity = asteroid_velocity

        return super().create(args)


class AsteroidManager(object):
    def __init__(self, asteroid_animations: list[Animation], screen: tuple[int,int]) -> None:
        self.asteroids = asteroid_animations

        self.spawn_points: list[pygame.Vector2] = [
            pygame.Vector2(-128, -128),
            pygame.Vector2(screen[0]/2, -128),
            pygame.Vector2(screen[0] + 128, -128),
            pygame.Vector2(screen[0] + 128, screen[1]/2),
            pygame.Vector2(screen[0] + 128, screen[1] + 128),
            pygame.Vector2(screen[0]/2, screen[1] + 128),
            pygame.Vector2(-128, screen[1] + 128),
            pygame.Vector2(-128, screen[1]/2)
        ]

        self.destination_points: list[pygame.Vector2] = [
            pygame.Vector2(screen[0]/2, screen[1]/2),
            pygame.Vector2(screen[0]/2 + 128, screen[1]/2),
            pygame.Vector2(screen[0]/2, screen[1]/2 - 128),
            pygame.Vector2(screen[0]/2 - 128, screen[1]/2),
            pygame.Vector2(screen[0]/2, screen[1]/2 + 128)
        ]
    
    def create_asteroid(self) -> Asteroid:
        current_spawn = self.spawn_points[random.randint(0,len(self.spawn_points) - 1)]
        current_destination = self.destination_points[random.randint(0,len(self.destination_points) - 1)]
        delta_x = current_destination.x - current_spawn.x
        delta_y = current_destination.y - current_spawn.y

        new_asteroid = Asteroid(
            "asteroid",
            self.asteroids[0],
            Transform(current_spawn.copy()),
            300
        )

        new_asteroid.create({
            "angle":math.atan2(delta_y, delta_x), 
            "pos":current_spawn.copy()
        })

        new_asteroid.start()
        return new_asteroid
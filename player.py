from typing import Any
import pygame
import math
from transform import Transform
from input_handler import InputHandler
from laser import Laser
from animation import Animation
from actor import Actor

class PlayerController(Actor):
    def __init__(self,
                 name: str, 
                 player_animation: Animation, 
                 play_pos: pygame.Vector2, 
                 key_configs: dict[str, int], 
                 player_speed: int, 
                 laser_animations: list[Animation],
                 laser_delay: float
                ) -> None:
        self.current_input =  InputHandler(key_configs)
        self.speed = player_speed
        self.mouse_pos: tuple[int,int]= (0,0)
        self.angle: float = 0
        self.lasers = laser_animations
        self.delta_x = 0
        self.delta_y = 0
        self.time = 0
        self.laser_delay = laser_delay
        self.can_shoot = True
        super().__init__(name, player_animation, Transform(play_pos))

    def is_accelerating(self) -> bool:
        answer = True if self.transform.velocity.magnitude() > 0 else False
        return answer
    
    def create_laser(self) -> Laser | None:
        if not self.can_shoot:
            return None

        # Calculate the starting position at the nose of the ship
        nose_offset = pygame.Vector2(
            (self.animation.current_frame.image.height / 2) * math.cos(math.radians(self.transform.direction)),
            -(self.animation.current_frame.image.height / 2) * math.sin(math.radians(self.transform.direction))
        )
        laser_start_pos = self.transform.position + nose_offset

        # Create the laser, passing a new Transform object with the correct starting position
        new_laser = Laser("new_laser", self.lasers[0], Transform(laser_start_pos), 500)

        # Call the create method to set the laser's velocity
        new_laser.create({
            "angle": math.atan2(-self.delta_y, self.delta_x), # The angle is in radians
            "player_pos": self.transform.position.copy(),
            "player_velocity": pygame.Vector2(0, 0)
        })

        new_laser.start()
        self.can_shoot = False
        return new_laser
    
    def start(self):
        return super().start()

    def update(self, dt, args: dict[str, Any]):
        self.time += dt
        if self.time >= self.laser_delay:
            if not self.can_shoot:
                self.can_shoot = True
            self.time = 0
        movement_direction = self.current_input.get_movement_vector()
        self.transform.position += movement_direction * self.speed * dt
        self.screen_wrap(args)
        self.mouse_pos = pygame.mouse.get_pos()
        self.delta_x = self.mouse_pos[0] - self.transform.position.x
        self.delta_y = self.mouse_pos[1] - self.transform.position.y
        self.transform.direction = math.degrees(math.atan2(-self.delta_y, self.delta_x))
        return super().update(dt, args)

    def screen_wrap(self, args: dict[str, Any]):
        if self.transform.position.x > args["screen"].width + 1:
            self.transform.position.x = 0
        if self.transform.position.x < -1:
            self.transform.position.x = args["screen"].width
        if self.transform.position.y > args["screen"].height + 1:
            self.transform.position.y = 0
        if self.transform.position.y < -1:
            self.transform.position.y = args["screen"].height
    
    def create(self, args: dict[str, Any]):
        return super().create(args)
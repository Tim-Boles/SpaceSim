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
                 laser_animations: list[Animation]
                ) -> None:
        self.current_input =  InputHandler(key_configs)
        self.speed = player_speed
        self.mouse_pos: tuple[int,int]= (0,0)
        self.angle: float = 0
        self.lasers = laser_animations
        self.delta_x = 0
        self.delta_y = 0
        super().__init__(name, player_animation, Transform(play_pos))

    def is_accelerating(self) -> bool:
        answer = True if self.transform.acceleration.magnitude() > 0 else False
        return answer
    
    def create_laser(self) -> Laser:
        new_laser = Laser("new_laser", self.lasers[0], Transform(self.transform.position), 360)
        new_laser.create(
            {
                "angle" : math.atan2(-self.delta_y, self.delta_x),
                "player_pos" : self.transform.position
            }
        )
        new_laser.start()
        return new_laser
    
    def start(self):
        return super().start()

    def update(self, dt, args: dict[str, Any]):
        self.transform.position += self.transform.acceleration * self.speed * dt
        self.mouse_pos = pygame.mouse.get_pos()
        self.delta_x = self.mouse_pos[0] - self.transform.position.x
        self.delta_y = self.mouse_pos[1] - self.transform.position.y
        self.transform.direction = math.degrees(math.atan2(-self.delta_y, self.delta_x))
        return super().update(dt, args)
    
    def create(self, args: dict[str, Any]):
        return super().create(args)
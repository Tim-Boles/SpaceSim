import pygame
import math
from transform import Transform

class Frame(object):
    def __init__(self, order: int, image: pygame.Surface):
        try:
            self.order = order
            self.image = image
        except pygame.error as e:
            print(e)

class Animation(object):
    def __init__(self, frames: list[Frame], loop: tuple[bool, int], fps: int, angel_offset: int):
        try:
            self.frames = frames
            self.loop = loop[0]
            self.hold_frame = frames[loop[1]]
            self.start_frame = frames[0]
            self.running = False
            self.ran = False
            self.time = 0
            self.current_frame = frames[0]
            self.count = 0
            self.frames_per_second = fps
            self.transform = Transform(pygame.Vector2(0,0))
            self.angel_offset = angel_offset
        except pygame.error as e:
            print(e)

    def start(self):
        if not self.running and not self.ran:
            self.running = True
            self.ran = False
        
    def reset(self):
        self.ran = False
        self.current_frame = self.start_frame

    def update(self, dt, transform: Transform, screen: pygame.Surface):
        self.time += dt
        if self.time >= ((1/self.frames_per_second)) and not self.ran:
            self.time = 0
            self.current_frame = self.frames[self.count]
            self.count += 1
            if (self.count == len(self.frames)):
                if self.loop:
                    self.count = 0
                else:
                    self.running = False
                    self.ran = True
                    self.count = 0
                    self.current_frame = self.hold_frame

        current_image = pygame.transform.rotate(
            self.current_frame.image, 
            transform.direction + self.angel_offset
        )
        current_rect = current_image.get_rect(
            center = transform.position
        )
        screen.blit(current_image, current_rect)
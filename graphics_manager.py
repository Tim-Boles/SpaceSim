import pygame
from spritesheet import SpriteSheet
from animation import Animation, Frame

class GraphicsManager(object):
    def __init__(self, sprite_sheets: dict[str, list[pygame.Vector2]]) -> None:
        # Set list of animations
        self.animations: dict[str,Animation] = {}

        # Load given spritesheets
        self.sprite_sheets: dict[str, SpriteSheet] = {}
        for key, value in sprite_sheets.items():
            self.sprite_sheets[key.split(".")[0]] = SpriteSheet(key, value[0], value[1], "black", value[2])

        # Build a sprite and its animation for the ship
        frame_1 = Frame(0, self.sprite_sheets["shipsprite1"].get_image(1))
        frame_2 = Frame(1, self.sprite_sheets["shipsprite1"].get_image(2))
        frame_3 = Frame(2, self.sprite_sheets["shipsprite1"].get_image(0))
        self.ship = Animation([frame_1, frame_2, frame_3], (False, 2), 1, -90)

        # Build a sprite and its animation for the laser
        frame_1 = Frame(0, self.sprite_sheets["M484BulletCollection2"].get_image(1409))
        frame_2 = Frame(1, self.sprite_sheets["M484BulletCollection2"].get_image(1410))
        frame_3 = Frame(2, self.sprite_sheets["M484BulletCollection2"].get_image(1411))
        frame_4 = Frame(3, self.sprite_sheets["M484BulletCollection2"].get_image(1412))
        self.laser = Animation([frame_1, frame_2, frame_3, frame_4], (True, 0), 30, 0)
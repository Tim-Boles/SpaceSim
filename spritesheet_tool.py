import pygame
import argparse
from spritesheet import SpriteSheet

parser = argparse.ArgumentParser(description="grids an image based on parameters")
parser.add_argument("-x", type=int, default=1)
parser.add_argument("-y", type=int, default=1)
parser.add_argument("-file")
parser.add_argument("-px", type=int, default=1)
parser.add_argument("-py", type=int, default=1)
parser.add_argument("-x_offset", type=int, default=0)
parser.add_argument("-y_offset", type=int, default=0)
args = parser.parse_args()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((args.x, args.y))
clock = pygame.time.Clock()
running = True
dt = 0
grid_mode = True
sprite_mode = False
sprite_sheet = SpriteSheet(args.file, 
                           pygame.Vector2(args.x, args.y), 
                           pygame.Vector2(args.px, args.py), 
                           "black", 
                           pygame.Vector2(args.x_offset, args.y_offset))
current_sprite = 0


while running:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    dt = max(0.001, min(0.1, dt))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and grid_mode:
                # Switch to sprite mode and display the clicked sprite
                columns_per_row = int(args.x/args.px)
                column = int((event.pos[0] - args.x_offset)/args.px)
                row = int((event.pos[1] - args.y_offset)/args.py)
                print(f"Col: {column} Row: {row}")
                index  = int((row * columns_per_row) + column)
                print(event.pos)
                print(index)
                grid_mode = False
                sprite_mode = True
                current_sprite = index
                break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Swap sprite modes
                if grid_mode:
                    sprite_mode = True
                    grid_mode = False
                else: 
                    grid_mode = True
                    sprite_mode = False
            # Go up and down the sprite sheet list
            if event.key == pygame.K_e:
                if sprite_mode:
                    current_sprite += 1
            if event.key == pygame.K_q:
                if sprite_mode:
                    current_sprite -= 1
    
    screen.fill("black")
    if grid_mode:
        image = sprite_sheet.sheet
        rect = image.get_rect()
        prev_x = args.x_offset
        prev_y = args.y_offset
        for y in range(0, int(args.y/args.py)):
            for x in range(0, int(args.x/args.px)):
                pygame.draw.rect(image, "white", [prev_x, prev_y, args.px, args.py], 1)
                prev_x += args.px
            prev_y += args.py
            prev_x = args.x_offset

        screen.blit(image, rect)
        pygame.display.flip()
    else:
        image = sprite_sheet.images[current_sprite]
        image = pygame.transform.scale(image, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
        rect = image.get_rect(center=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(f"{current_sprite}", True, "red")
        image.blit(text, (0,0))
        screen.blit(image, rect)
        pygame.display.flip()
        
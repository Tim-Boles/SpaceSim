import pygame
from player import PlayerController
from graphics_manager import GraphicsManager
from actor import Actor
FPS = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

graphics_manager = GraphicsManager(
    {
        "shipsprite1.png" : [pygame.Vector2(192,512), pygame.Vector2(64,64), pygame.Vector2(0,0)],
        "M484BulletCollection2.png" : [pygame.Vector2(1420,760), pygame.Vector2(16,16), pygame.Vector2(0,7)]
    }
)

# Player Controller
key_configs = {
    "w" : pygame.K_w,
    "a" : pygame.K_a,
    "s" : pygame.K_s,
    "d" : pygame.K_d,
    "mb_1" : pygame.BUTTON_LEFT
}

# All Actors
actors: list[Actor] = []
# Lasers
laser_actors = []
# Asteroids
asteroid_actors = []

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_controller = PlayerController(
    "ship", 
    graphics_manager.ship, 
    player_pos,
    key_configs, 
    300, 
    [graphics_manager.laser],
    0.1
)
player_controller.start()
player_controller.create({"angle":0, "pos":player_pos})
actors.append(player_controller)

clicked = (False, pygame.Vector2(0,0))
context = ("Combat", 0)

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000
    dt = max(0.001, min(0.1, dt))

    input_events = (pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type in input_events:
            player_controller.current_input.handle_event(event)
            player_controller.transform.acceleration = player_controller.current_input.get_movement_vector()
            clicked = player_controller.current_input.handle_click(event)
    
    if player_controller.is_accelerating():
        if not player_controller.animation.running:
            player_controller.animation.start()
    else:
        player_controller.animation.reset()

    if clicked[0] and context[0] == "Combat":
        new_laser = player_controller.create_laser()
        if new_laser:
            actors.append(new_laser)
            laser_actors.append(new_laser)

    for actor in actors:
        actor.update(dt, {"screen": screen})
    # flip() the display to put your work on screen
    pygame.display.flip()

    
    
    

pygame.quit()
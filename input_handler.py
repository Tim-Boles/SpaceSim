import pygame

class InputHandler(object):
    def __init__(self, player_movement_keys: dict[str, int]) -> None:
        self.player_movement_keys = player_movement_keys
        self.current_input = {}

    def handle_event(self, event: pygame.Event) -> None:
        """Updates the dictionary of currently pressed keys."""
        down_events = (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN)
        up_event = (pygame.KEYUP, pygame.MOUSEBUTTONUP)
        if event.type in down_events:
            self.current_input[event.key if event.type == pygame.KEYDOWN else f"mb_{event.button}"] = True
        elif event.type in up_event:
            self.current_input.pop(event.key if event.type == pygame.KEYUP else f"mb_{event.button}", None)

    def handle_click(self, event: pygame.Event) -> tuple[bool, pygame.Vector2]:
        """Resolves any mouse clicks in the Frame"""
        if "mb_1" in self.current_input.keys():
            if self.current_input["mb_1"] == True:
                print("I clicked")
                self.current_input["mb_1"] = False
                return (True, event.pos)
        return (False, pygame.Vector2(0,0))   
    def get_movement_vector(self) -> pygame.Vector2:
        """
        Calculates the movement vector based on the currently pressed keys.
        This should be called once per game loop.
        """
        vec = pygame.Vector2(0, 0)

        # Check for movement keys in the dictionary of currently held keys
        if self.player_movement_keys.get('w') in self.current_input:
            vec.y -= 1
        if self.player_movement_keys.get('s') in self.current_input:
            vec.y += 1
        if self.player_movement_keys.get('a') in self.current_input:
            vec.x -= 1
        if self.player_movement_keys.get('d') in self.current_input:
            vec.x += 1
        
        # Normalize the vector to prevent faster diagonal movement
        if vec.length() > 0:
            vec.normalize_ip()
            
        return vec

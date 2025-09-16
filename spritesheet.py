import pygame

class SpriteSheet(object):
    def __init__(self, file_name: str, height_width: pygame.Vector2, p_height_width: pygame.Vector2, color_key, offset_vec: pygame.Vector2):
        try:
            self.sheet = pygame.image.load(file_name).convert_alpha()
            self.width = height_width.x
            self.height = height_width.y
            self.p_width = p_height_width.x
            self.p_height = p_height_width.y
            self.x_offset = offset_vec.x
            self.y_offset = offset_vec.y
            self.color_key = color_key 
            self.images = self.set_images()   
        except pygame.error as e:
            print(e)
    
    def get_image(self, index) -> pygame.Surface:
        return self.images[index]
    
    def make_image(self, rectangle: pygame.Rect) -> pygame.Surface:
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        if self.color_key:
            image.set_colorkey(self.color_key)
        image.blit(self.sheet, (0, 0), rect)
        return image
    
    def set_images(self) -> list[pygame.Surface]:
        c_image: list[pygame.Surface] = []
        x_pos = self.x_offset
        y_pos = self.y_offset
        for y in range(int(self.height/self.p_height)):
            for x in range(int(self.width/self.p_width)):
                rect = pygame.Rect((x_pos, y_pos, self.p_width, self.p_height))
                c_image.append(self.make_image(rect))
                x_pos += self.p_width  
            y_pos += self.p_height
            x_pos = self.x_offset
        return c_image
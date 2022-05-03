import pygame
from modules.colors import *


class Button:
    def __init__(self, text, pos_x, pos_y, width,height,elevation, mySurface):
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.surface = mySurface
        self.pressed = False


        # top rectangle 
        self.top_rect = pygame.Rect((pos_x, pos_y),(width,height))
        self.top_color = GREY

        # bottom rectangle 
        self.bottom_rect = pygame.Rect((pos_x, pos_y),(width,height))
        self.bottom_color = BLACK

        self.text = text

        self.text_surface = mySurface
        self.text_surface = pygame.font.Font(None,30).render(text,True,WHITE)
        
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic 
        self.top_rect.y = self.pos_y - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(self.surface, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(self.surface, self.top_color, self.top_rect, border_radius = 12)

        self.surface.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = ROSE
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = GREY


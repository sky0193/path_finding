from typing import Tuple
import pygame
import view_helper.colors

class Button:
    def __init__(self, text: str, pos_x: int, pos_y: int, width: int, height: int,
                 elevation: int, mySurface: pygame.surface.Surface):

        self.elevation: int = elevation
        self.dynamic_elecation: int = elevation
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.surface: pygame.surface.Surface = mySurface
        self.pressed: bool = False

        # top rectangle
        self.top_rect: pygame.rect.Rect = pygame.Rect((pos_x, pos_y), (width, height))
        self.top_color: Tuple[int, int, int] = view_helper.colors.GREY

        # bottom rectangle
        self.bottom_rect: pygame.rect.Rect = pygame.Rect((pos_x, pos_y), (width, height))
        self.bottom_color: Tuple[int, int, int] = view_helper.colors.BLACK

        self.text: str = text

        self.text_surface: pygame.surface.Surface = mySurface
        self.text_surface = pygame.font.Font(None, 30).render(text, True, view_helper.colors.WHITE)

        self.text_rect: pygame.rect.Rect = self.text_surface.get_rect(center=self.top_rect.center)

    def draw(self) -> None:
        # elevation logic
        self.top_rect.y = self.pos_y - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(self.surface, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.surface, self.top_color, self.top_rect, border_radius=12)

        self.surface.blit(self.text_surface, self.text_rect)
        self.check_click()

    def check_click(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = view_helper.colors.ROSE
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    print('click')
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = view_helper.colors.GREY

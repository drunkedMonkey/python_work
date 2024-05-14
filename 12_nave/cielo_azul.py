import pygame
from bald import Bald

class CieloAzul:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cielo Azul")

        self.bald = Bald(self)

        self.bg_color = (0, 0, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(self.bg_color)
            self.bald.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    cielo_azul = CieloAzul()
    cielo_azul.run_game()
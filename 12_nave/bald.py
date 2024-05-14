import pygame

class Bald:
    def __init__(self, bald_game):
        self.screen = bald_game.screen
        self.screen_rect = bald_game.screen.get_rect()

        self.image = pygame.image.load('./12_nave/bald.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
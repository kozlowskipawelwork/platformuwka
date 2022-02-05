
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):#,disp
        pygame.sprite.Sprite.__init__(self)
        self.player_sprite = pygame.image.load('data/img/joy of the fallen heroes.png').convert_alpha()
        self.screen_width = 800
        self.screen_height = 640
        self.rect = self.player_sprite.get_rect()
        self.rect.x = self.screen_width/2-35
        self.rect.y = self.screen_height/2 -35
        self.hp = 100
        self.speed = 10
        self.strength = 10

    def draw(self):
        print(self.hp)
        screen.blit(self.player_sprite, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x-400, self.rect.y -280, 100, 5))
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x -400, self.rect.y - 280, self.hp//2, 10))

    def rect_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.centerx += -self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.centerx += self.speed
        if keys[pygame.K_UP]:
            self.y += -self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed



    def update(self):
        #hmm, czemu nie musze callowac rect_movement?
        self.draw()






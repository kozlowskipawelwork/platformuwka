from player import *
import pygame

class Stone():
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.screen_width = 800
        self.screen_height = 640
        self.speed = 10
        self.stone_sprite = pygame.image.load('data/img/jofth stone 1.png').convert_alpha()
        self.rect = self.stone_sprite.get_rect()
        self.rect.x = 300
        self.rect.y = 300

    def draw(self):
        screen.blit(self.stone_sprite, (self.rect.x, self.rect.y))

    def collision(self):
        pass
        if self.rect.colliderect(self.player.rect):
            print("collision")

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x += self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += -self.speed
        if keys[pygame.K_UP]:
            self.rect.y += self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += -self.speed

    def update(self):
        self.move()
        self.collision()
        self.draw()

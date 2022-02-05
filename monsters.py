import pygame
from settings import *
from player import *
from bullets import Weapon


class Monster1():
    def __init__(self):
        self.x = 600
        self.y = 400
        self.speed = 10
        self.hp = 10
        self.strength = 2
        self.monster1_sprite = pygame.image.load('data/img/blood surfer.png')

    def draw(self):
        screen.blit(self.monster1_sprite, (self.x, self.y))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += -self.speed
        if keys[pygame.K_UP]:
            self.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.y += -self.speed
    def update(self):
        self.move()
        self.draw()

class Monster2(pygame.sprite.Sprite):
    def __init__(self,player, weapon):
        pygame.sprite.Sprite.__init__(self)

        self.player = player
        self.weapon = weapon
        #self.bullets = bullets
        self.screen_width = 800 #niekoniecznie potrzebne
        self.screen_height = 640 #niekoniecznie potrzebne
        self.hp = 100 #hp potwora, do zastosowania potem
        self.monster_strength = 200
        self.speed = 10
        self.monster2_sprite = pygame.image.load('data/img/crab ascendant.png')
        self.rect = self.monster2_sprite.get_rect()
        self.rect.x = 2000
        self.rect.y = 250
        self.monster2_dead = False

    def draw(self):
        if self.hp > 0:
            screen.blit(self.monster2_sprite, (self.rect.x, self.rect.y))
            pygame.draw.rect(screen,(0,0,0),(self.rect.x +75, self.rect.y+50,100,5))
            pygame.draw.rect(screen, (255, 0, 0), (self.rect.x + 75, self.rect.y + 50, self.hp, 5))

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

    def collision(self):
        if self.hp > 0:
            if self.rect.colliderect(self.player.rect):
                print("potwor dotyka playera")
                self.player.hp += -1
            if self.player.rect.colliderect(self.rect):
                print("player dotyka potwora")
                self.hp += -1
        if self.weapon.rect.colliderect(self.rect):
                self.hp += -3


    def update(self):
        self.collision()
        self.move()
        self.draw()

class Postac(pygame.sprite.Sprite):
    def __init__(self,player, weapon):
        pygame.sprite.Sprite.__init__(self)

        self.player = player
        self.weapon = weapon
        #self.bullets = bullets
        self.screen_width = 800 #niekoniecznie potrzebne
        self.screen_height = 640 #niekoniecznie potrzebne
        self.hp = 10 #hp potwora, do zastosowania potem
        self.monster_strength = 200
        self.speed = 10
        self.monster2_sprite = pygame.image.load('data/img/Golden Saint.png')
        self.rect = self.monster2_sprite.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.monster2_dead = False

    def draw(self):
        if self.hp > 0:
            screen.blit(self.monster2_sprite, (self.rect.x, self.rect.y))
            pygame.draw.rect(screen,(0,0,0),(self.rect.x +75, self.rect.y+50,10,5))
            pygame.draw.rect(screen, (255, 0, 0), (self.rect.x + 75, self.rect.y + 50, self.hp, 5))

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

    def collision(self):
        if self.hp > 0:
            if self.rect.colliderect(self.player.rect):
                print("potwor dotyka playera")
                self.player.hp += -1
            if self.player.rect.colliderect(self.rect):
                print("player dotyka potwora")
                self.hp += -1
        if self.weapon.rect.colliderect(self.rect):
                self.hp += -3


    def update(self):
        self.collision()
        self.move()
        self.draw()
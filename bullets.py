from player import *
import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen_width = 800 #szrokosc ekranu okresla zmienna za pomoca ktorej pozycjonuje sie bron na srodku ekranu
        self.screen_height = 640 #szrokosc ekranu okresla zmienna za pomoca ktorej pozycjonuje sie bron na srodku ekranu to jest chyba w ogole zle nazwane XD
        self.speed = 50 #predkosc z jaka porusza sie bron
        #self.strength = 10 moze odwolanie do player strenght w przyszlosci?
        self.weapon_sprite = pygame.image.load('data/img/weapons/possesed war axe.png').convert_alpha() #sprowadza obraz broni - tutaj wywolujesz bron, moze potem zrobic
        self.rect = self.weapon_sprite.get_rect()  #tworzy rect na sprajcie, w celu poruszania nim wraz z kolizjami. (nie ruszac samym obrazkiem tylko rectem)
        self.rect.x = self.screen_width/2-35 #ustala rect broni na srodku
        self.rect.y = self.screen_height/2-35 #ustawia rect broni na srodku

    def draw(self):
        screen.blit(self.weapon_sprite, (self.rect.x, self.rect.y))#rysuje sprajta na pozycji recta, one sa jakby razem teraz

    def move(self):
        keys = pygame.key.get_pressed() #funkcja wywolujaca player input i przypisujaca ja do zmiennej keys
        if (keys[pygame.K_LEFT] and keys[pygame.K_UP]):
            if keys[pygame.K_c]:
                self.rect.x -= self.speed
                self.rect.y -= self.speed
        elif (keys[pygame.K_RIGHT] and keys[pygame.K_UP]):
            if keys[pygame.K_c]:
                self.rect.x += self.speed
                self.rect.y -= self.speed
        elif (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]):
            if keys[pygame.K_c]:
                self.rect.x += self.speed
                self.rect.y += self.speed
        elif (keys[pygame.K_LEFT] and keys[pygame.K_DOWN]):
            if keys[pygame.K_c]:
                self.rect.x -= self.speed
                self.rect.y += self.speed
        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_c]:
                self.rect.y += self.speed
        elif keys[pygame.K_UP]:
            if keys[pygame.K_c]:
                self.rect.y -= self.speed
        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_c]:
                self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_c]:
                self.rect.x += self.speed
        else: #jesli nic sie nie dzieje,
            self.rect.x = self.screen_width/2-35 #self.rect.x przesuwa sie na srodek ekranu
            self.rect.y = self.screen_height/2 -35 #self.rect.y przesuwa sie na srodek ekranu

    def update(self):#korzystasz przy przywolywaniu sprajta w mainie
        self.move()
        self.draw()
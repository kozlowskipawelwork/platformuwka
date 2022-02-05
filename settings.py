import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
screen_width = 800
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('platformuwka')

#x granica i plowoa szerokosci ekranu w lewej krawedzi odjac ogarnac zeby nie widzial ze tlo sie przesuwa
#load images
#background image
class Background():
    def __init__(self):#disp
        pygame.sprite.Sprite.__init__(self)
        self.bottom_panel = 1240
        self.screen_width = 800
        self.screen_height = 640
        self.x = self.screen_width/2-35
        self.y = self.screen_height/2 -35
        #self.x = disp[0]#disp to lista, ktora zawiera w sobie x i y, i zbiera je ze zmiennej system settings z maina.
        #self.y = disp[1]#x i y rownaja sie polowie wysokosci i szerokosci ekranu podzielic przez 2
        self.speed = 10
        self.background_img = pygame.image.load('data/img/sofh sky.png').convert_alpha()
#panel image
        self.panel_img = pygame.image.load('data/img/tile 3.png').convert_alpha()
#function for drawing background
    def draw_bg(self):
        screen.blit(self.background_img, (self.x, self.y))
#function for drawing panel
    def draw_panel(self):
        #mozna pododawac potem po 5 dla efektu pocietej podlogi
        screen.blit(self.panel_img, (self.x-self.screen_width/2,self.y-self.screen_height/2))
        screen.blit(self.panel_img, (self.x - self.screen_width / 2, self.y - self.screen_height - 880)) #gorny
        screen.blit(self.panel_img, (self.x - self.screen_width / 2, self.y - self.screen_height + 1520)) #dolny
        screen.blit(self.panel_img, (self.x - self.screen_width-800, self.y - self.screen_height/2))#lewy
        screen.blit(self.panel_img, (self.x - self.screen_width + 1600, self.y - self.screen_height / 2))#prawy
        screen.blit(self.panel_img, (self.x - self.screen_width / 2+ 1200, self.y - self.screen_height / 2-1200))#prawygorny
        screen.blit(self.panel_img, (self.x - self.screen_width / 2 - 1200, self.y - self.screen_height / 2-1200))#lewygorny
        screen.blit(self.panel_img, (self.x - self.screen_width / 2 + 1200, self.y - self.screen_height / 2+1200))#prawydolny
        screen.blit(self.panel_img, (self.x - self.screen_width / 2 - 1200, self.y - self.screen_height / 2 + 1200))#lewydolny

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x += self.speed
            if self.x > 880:
                self.x = -325
        if keys[pygame.K_RIGHT]:
            self.x += -self.speed
            if self.x < -325:
                self.x = 880
        if keys[pygame.K_UP]:
            self.y += self.speed
            if self.y > 675:
                self.y = -520
        if keys[pygame.K_DOWN]:
            self.y += -self.speed
            if self.y < -520:
                self.y = 675

    def update(self):
        #print(self.x,self.y)
        self.move()
        self.draw_bg()
        self.draw_panel()


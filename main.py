import pygame

from items import *
import settings
from settings import *


from monsters import *
from bullets import *
from player import *


screen_settings = (settings.screen_width/2-35, settings.screen_height/2-35) #znajduje x i y srodka ekranu
player = Player() #inwokuje bohatera na srodku ekranu
monster = Monster1() #inwokuje pierszego potwora
weapon = Weapon()#bron bohatera
crab_ascendant = Monster2(player,weapon) #inwokuje drugiego potwora.
ue = Postac(player, weapon)


background = Background()#inwokuje background na srodku ekranu.

stone = Stone(player)#kamien
run = True
while run:

    clock.tick(fps)
    # draw background
    background.update()
    ue.update()

    #weapon
    weapon.update()
    #monster.update()
    crab_ascendant.update()
    player.update()
    stone.update()
    #pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 30, 60, 60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    if player.hp == 0:
        break

pygame.quit()
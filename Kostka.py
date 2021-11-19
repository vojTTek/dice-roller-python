import pygame
import pygame_menu
from random import randrange
pygame.init()
surface = pygame.display.set_mode((400, 400))
def kostki(x,y):
     global a
     global b
     a=x
     b=y
     pass
def rzut():

menu = pygame_menu.Menu('Dice Roller', 400, 400,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Wybierz kostkę', [('k4', 4), ('k6', 6), ('k8', 8), ('k10', 10), ('k12', 12), ('k20', 20), ('k100/%', 100)], onchange=kostki)
menu.add.text_input('wpisz ilość rzutów: ', s=1)
menu.add.text_input('wpisz wartość sukcesu: ', q=1)
menu.add.button('Rzucaj', rzut)
menu.add.button('Koniec', pygame_menu.events.EXIT)
menu.mainloop(surface)

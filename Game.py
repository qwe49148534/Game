import pygame
import os
from pygame.constants import QUIT

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_pannel = 150
screen_width = 800
screen_height = 400 + bottom_pannel

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Battle')

#load images

#background image
background_img = pygame.image.load('img/Background/background.png').convert_alpha()

#panel_img
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

#function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))

#panel_fuciton
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_pannel))

class Fighter():
    def __init__(self, x, y , name , max_hp , strength , potions):
        self.name = name
        self.max_hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        img = pygame.image.load(f'img/{self.name}/Idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width * 3 , img.get_height))
        self.rect = self.image.get_rect()
        self.rect.ceter = (x , y) 

    def draw(self):
        screen.bilt(self.image, self.rect)

Knight = Fighter( 200, 260,'Knight' , 30, 10, 3)

run = True
while run:

    clock.tick(fps)

    #draw background
    draw_bg()

    #draw panel
    draw_panel()

    #draw fighter
    Knight.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()

pygame.quit()
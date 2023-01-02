#!/bin/python3

# import
import math
import pygame
from pygame.locals import *
from carte import *
from joueur import *
from ray import *

# initialisation
height, width = 960, 1820

#color
white = (255, 255, 255)
black = (0, 0, 0)

# fenetre
pygame.init()
fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption('raycasting')

#auto
AUTOFPS = USEREVENT + 1
pygame.time.set_timer(AUTOFPS, 32)

#Déplacement maintenue
pygame.key.set_repeat(10, 30)

# carte
carte = Carte(fenetre, "map.txt")

# angle
listRay = [Ray(fenetre, i/10000, carte, i//25) for i in range(0, 3000, 25)]

# joueur
joueur = Joueur(fenetre, "joueur.xcf", [100, 100], listRay)

# boucle infini
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        
        if event.type == AUTOFPS:
            fenetre.fill(white)
            carte.afficheAll()
            joueur.afficheAll()
            pygame.display.flip()

        # keyboard
        if event.type == KEYDOWN :
            joueur.deplacement(event.key)
            if event.key == K_ESCAPE:
                continuer = False

        #souris
        if event.type == MOUSEMOTION:
            #joueur.deplacement(pygame.mouse.get_pos())
            if pygame.mouse.get_pressed()[2]:
                carte.enleve(event.pos)

            if pygame.mouse.get_pressed()[0]:
                carte.ajoute(event.pos)
       
# quit
pygame.quit()


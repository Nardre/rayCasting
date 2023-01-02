# import
import pygame
from pygame.locals import *
import math

class Joueur:
    def __init__(self, fenetre, nom, pos, listRay):
        self.fenetre = fenetre
        self.nom = pygame.image.load(f"images/{nom}").convert_alpha()
        self.pos = pos
        self.listRay = listRay
        self.angle = 0.14875


    def afficheAll(self):
        x, y = self.pos
        self.fenetre.blit(self.nom, (x-16, y-16))
        for ray in self.listRay:
            ray.afficheAll(self.pos, self.angle)

    def deplacement(self, key):
        if key==K_z:
            self.pos[0] += math.cos(self.angle*math.pi)*10
            self.pos[1] += math.sin(self.angle*math.pi)*10
        if key==K_s:
            self.pos[0] -= math.cos(self.angle*math.pi)*10
            self.pos[1] -= math.sin(self.angle*math.pi)*10
        if key==K_q:
            self.pos[0] -= math.cos((self.angle+0.5) * math.pi)*10
            self.pos[1] -= math.sin((self.angle+0.5) * math.pi)*10
        if key==K_d:
            self.pos[0] -= math.cos((self.angle-0.5) * math.pi)*10
            self.pos[1] -= math.sin((self.angle-0.5) * math.pi)*10

        if key==K_e:
            self.angle = (self.angle + 0.025) %2
            for ray in self.listRay:
                ray.tourne(0.025)
        
        if key==K_a:
            self.angle = (self.angle - 0.025) %2
            for ray in self.listRay:
                ray.tourne(-0.025)



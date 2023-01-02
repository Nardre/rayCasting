# import
import pygame
from pygame.locals import *
import math

class Carte:
    def __init__(self, fenetre, carte):
        self.fenetre = fenetre
        self.carte = []
        
        self.black = (0, 0, 0)
        
        with open(carte, "r") as file:
            for line in file:
                self.carte += [list(map(int, line[:-1]))]
            file.close()        
    
    def afficheAll(self):
        for y in range(len(self.carte)):
            for x in range(len(self.carte[y])):
                if self.carte[y][x]==1:
                    pygame.draw.rect(self.fenetre, (self.black), [x*32, y*32, 32, 32])

    def ajoute(self, pos):
        x, y = pos[0]//32, pos[1]//32
        if x>=0 and y>=0 and x<30 and y<30:
            self.carte[y][x] = 1

    def enleve(self, pos):
        x, y = pos[0]//32, pos[1]//32
        if x>=0 and y>=0 and x<30 and y<30:
            self.carte[y][x] = 0

    def est_libre(self, x, y):
        x = int(x//32)
        y = int(y//32)
        if x<0 or y<0 or x>=30 or y>=30:
            return 0
        return self.carte[y][x] == 0




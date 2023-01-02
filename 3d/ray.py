# import
import pygame
from pygame.locals import *
import math

class Ray:
    def __init__(self, fenetre, angle, carte, pos3d):
        self.fenetre = fenetre
        self.angle = angle
        self.carte = carte
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.pos3d = pos3d

    def afficheAll(self, pos, joueurAngle):
        angle = self.angle * math.pi
        x, y = pos
        xMap, yMap = int(x//32) * 32, int(y//32) * 32
        sin = math.sin(angle) + 0.0001
        cos = math.cos(angle) + 0.0001
        
        # horizontal
        if sin>0:
            yHori = yMap + 0.000001
            dy = 32
        else:
            yHori = yMap - 0.000001
            dy = -32
        hHori = (yHori - y) / sin
        xHori = x + hHori*cos
        
        dh = dy / sin
        dx = dh * cos
        
        while self.carte.est_libre(xHori, yHori):
            xHori += dx
            yHori += dy
            hHori += dh

        # verticale
        if cos>0:
            xVert = xMap + 0.000001
            dx = 32
        else:
            xVert = xMap - 0.000001
            dx = -32

        hVert = (xVert - x) / cos
        yVert = y + hVert*sin
        
        dh = dx / cos
        dy = dh * sin

        while self.carte.est_libre(xVert, yVert):
            xVert += dx
            yVert += dy
            hVert += dh
        
        # 2d
        if hHori<hVert and hHori>0 or hVert<0:
            minPos = (xHori, yHori)
            minH = hHori
            couleur = (50, 50, 50)
        else:
            minPos = (xVert, yVert)
            minH = hVert
            couleur = (25, 25, 25)

        pygame.draw.line(self.fenetre, self.black, pos, minPos)

        # 3d
        
        # fisheye
        fisheye = abs(joueurAngle - self.angle) * math.pi
        
        minH *= math.cos(fisheye)
        murH = 32*960 / minH
        murH = 960 if murH>960 else murH
        murY = 480 - murH/2
        pygame.draw.rect(self.fenetre, couleur, [970 + self.pos3d*7, murY, 7, murH])


    def tourne(self, angle):
        self.angle = (self.angle + angle) %2
















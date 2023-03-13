import pygame
import colorswatch as cs
from enum import Enum

class Pixel(object):
    def __init__(self, surface, posX, posY, color):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color
        self.size = 2
        self.pixel_block = pygame.Rect(self.posX, self.posY, self.size, self.size)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.pixel_block)




class Character(object):
    def __init__ (self, surface, posX, posY, isPlayer = False):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.speed = 5
        self.isPlayer = isPlayer


    def build(self):
        # TODO: Build and sprite images
        pass

    def draw(self):
        # TODO: Draw the sprite images
        pass

    def move(self, direction):
        # TODO: Animation logic goes here
        pass

    def collision_manager(self):
        # TODO: Collision handling
        pass

    def update(self):
        # TODO: Update method
        pass
import pygame
import colorswatch as cs
from enum import Enum

template = ["----000000----",
            "---0------0---",
            "---0------0---",
            "--0--0--0--0--",
            "--0--0--0--0--",
            "---0------0---",
            "--000----000--",
            "-0---0000---0-",
            "0--0------0--0",
            "0--0------0--0",
            "-000------000-",
            "---0------0---",
            "---00000000---",
            "---00000000---",
            "---00000000---",
            "---00000000---",
            "----00--00----"]

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
        self.health = 100
        self.level = 0
        self.inventory = []
        self.name = None
        self.species = None


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

class Harriman(Character):
    def __init__(self, surface, posX, posY, isPlayer = True):
        super().__init__(surface, posX, posY, isPlayer)
        self.sprite_sheet = []
        self.sprite_strip = []
        self.name = "Harriman"
        self.species = "Human"
        self.level = 6
        self.templates = [["----000000----",
                           "---0GGGGGG0---",
                           "---0FFFFFF0---",
                           "--0FF0FF0FF0--",
                           "--0FF0FF0FF0--",
                           "---0FFGGFF0---",
                           "--000GFFG000--",
                           "-0RRW0000RRR0-",
                           "0RR0W-RGYG0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGYGG0000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "---00000000---",
                           "---00000000---",
                           "----00--00----"],

                          ["----000000----",
                           "---0GGGGGG0---",
                           "---0GGGGGG0---",
                           "--0GGGGGGGG0--",
                           "--0GGGGGGGG0--",
                           "---0GGGGGG0---",
                           "--000FFFF000--",
                           "-0RRR0000RWR0-",
                           "0RR0RRRRRR0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGRRGG000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "---00000000---",
                           "---00000000---",
                           "----00--00----"],

                          ["----000000----",
                           "---0GGGGGG0---",
                           "---0FFFFFF0---",
                           "--0FF0FF0FF0--",
                           "--0FF0FF0FF0--",
                           "---0FFGGFF0---",
                           "--000GFFG000--",
                           "-0RRW0000RRR0-",
                           "0RR0W-RGYG0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGYGG0000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "---0000-------",
                           "---0000-------",
                           "----00--------"],

                          ["----000000----",
                           "---0GGGGGG0---",
                           "---0FFFFFF0---",
                           "--0FF0FF0FF0--",
                           "--0FF0FF0FF0--",
                           "---0FFGGFF0---",
                           "--000GFFG000--",
                           "-0RRW0000RRR0-",
                           "0RR0W-RGYG0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGYGG0000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "-------0000---",
                           "-------0000---",
                           "--------00----"],

                          ["----000000----",
                           "---0GGGGGG0---",
                           "---0GGGGGG0---",
                           "--0GGGGGGGG0--",
                           "--0GGGGGGGG0--",
                           "---0GGGGGG0---",
                           "--000FFFF000--",
                           "-0RRR0000RWR0-",
                           "0RR0RRRRRR0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGRRGG000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "---0000-------",
                           "---0000-------",
                           "----00--------"],

                          ["----000000----",
                           "---0GGGGGG0---",
                           "---0GGGGGG0---",
                           "--0GGGGGGGG0--",
                           "--0GGGGGGGG0--",
                           "---0GGGGGG0---",
                           "--000FFFF000--",
                           "-0RRR0000RWR0-",
                           "0RR0RRRRRR0RR0",
                           "0FF0RRRRRR0FF0",
                           "-000GGRRGG000-",
                           "---0RRRRRR0---",
                           "---00000000---",
                           "---00000000---",
                           "-------0000---",
                           "-------0000---",
                           "--------00----"]
                          ]


    def build(self, index):
        #super().build()
        x, y = self.posX, self.posY

        for row in self.templates[index]:
            for col in row:
                if col == "0":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.black["pygame"]))
                if col == "B":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.brown["pygame"]))
                if col == "F":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.flesh["pygame"]))
                if col == "G":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.night_gray["pygame"]))
                if col == "R":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.monster_maroon["pygame"]))
                if col == "Y":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.yellow["pygame"]))
                if col == "W":
                    self.sprite_sheet.append(Pixel(self.surface, x, y, cs.white["pygame"]))

                x += 2

            y += 2
            x = self.posX

    def get_sprite(self, index):
        self.build(index)

    def draw(self):
        for pixel in self.sprite_sheet:
            pixel.draw()
import colorswatch as cs
import pygame

# This is the sprite base for all sprites

cross = 14
updown = 17
size = 2

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




generic = ["----000000----",
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


captain = ["----000000----",
           "---0BBBBBB0---",
           "---0FFBBFF0---",
           "--0FF0FF0FF0--",
           "--0FF0FF0FF0--",
           "---0FFFFFF0---",
           "--000FFFF000--",
           "-0RRW0000RRR0-",
           "0RR0W-RGYG0RR0",
           "0FF0RRRRRR0FF0",
           "-000GGYGG0000-",
           "---0RRRRRR0---",
           "---00000000---",
           "---00000000---",
           "---00000000---",
           "---00000000---",
           "----00--00----"]
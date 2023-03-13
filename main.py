import pygame
import colorswatch as cs
import spritebase

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)

pygame.init()

SURFACE = pygame.display.set_mode(SCREEN)
CLOCK = pygame.time.Clock()
FPS = 60
BG = cs.cornflower_blue["pygame"]

captain_sprite = []

def build_captain():
    global captain_sprite

    x_origin = SCREEN_X / 2
    y_origin = SCREEN_Y / 2

    x, y = x_origin, y_origin

    for row in spritebase.captain:
        for col in row:
            if col == "0":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.black["pygame"]))
            if col == "B":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.brown["pygame"]))
            if col == "F":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.flesh["pygame"]))
            if col == "G":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.night_gray["pygame"]))
            if col == "R":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.monster_maroon["pygame"]))
            if col == "Y":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.yellow["pygame"]))
            if col == "W":
                captain_sprite.append(spritebase.Pixel(SURFACE, x, y, cs.white["pygame"]))

            x += 2

        y += 2
        x = x_origin



def draw():
    for pixel in captain_sprite:
        pixel.draw()

def main():
    inPlay = True
    build_captain()

    while inPlay:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            inPlay = False


        draw()
        pygame.display.update()
        SURFACE.fill(BG)

if __name__ == "__main__":
    main()
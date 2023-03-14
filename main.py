import pygame
import colorswatch as cs
import character

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)

pygame.init()

SURFACE = pygame.display.set_mode(SCREEN)
CLOCK = pygame.time.Clock()
FPS = 60
BG = cs.cornflower_blue["pygame"]

captain_harriman = character.Harriman(SURFACE, 320, 240)



def build_all():
    captain_harriman.get_sprite(0)

def draw():
    captain_harriman.draw()


def main():
    inPlay = True
    build_all()

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
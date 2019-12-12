import random
import pygame
from multiprocessing import Pool

WIDTH = 200
HEIGHT = 200

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Sort")
clock = pygame.time.Clock()

def change_screen(colorshere):
    for i in colorshere:
        game_display.set_at((i[1], i[2]), i[0])
    pygame.display.update()
    
def get_random_color():
    color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return color

def make_color_list():
    colors = []
    #Note Data format comes out as [[R,G,B], Width, Height]
    for w in range(0,WIDTH):
        for h in range(0,HEIGHT):
            colors.append([get_random_color(),w,h])
    return colors

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        change_screen(make_color_list())
        clock.tick(60)
    
if __name__ == "__main__":
    main()

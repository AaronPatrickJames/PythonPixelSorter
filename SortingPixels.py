import random
import pygame
from multiprocessing import Pool

WIDTH = 300
HEIGHT = 300

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Sort")
clock = pygame.time.Clock()

def change_screen(colorshere):
    for i in colorshere:
        game_display.set_at((i[1], i[2]), i[0])
        pygame.display.update()
    return colorshere

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

def bubble_sort(bubArr):
    for item in range(len(bubArr)-1,0,-1):
        for i in range(num):
            if bubArr[i]>= bubArr[i+1]:
                temp = bubArr[i]
                bubArr[i] = bubArr[i+1]
                bubArr[i+1] = temp
            
    print("Bubble: \n" + str(bubArr))
    print("")
    return True



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        sort_me = change_screen(make_color_list())
        clock.tick(60)
        #This is where my sorts would go
        #IF I HAD THEM
        am_i_done = bubble_sort(sort_me)
        

        
    
if __name__ == "__main__":
    main()

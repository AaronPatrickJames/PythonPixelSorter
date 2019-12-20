import random
import pygame
from multiprocessing import Pool

WIDTH = 500
HEIGHT = 500

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Sort")
clock = pygame.time.Clock()

def change_screen(colorshere):
    for i in colorshere:
        game_display.set_at((i[1], i[2]), get_random_color())
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

def swap_pixels(values):
    pass
    
def bubble_sort(bubArr):
    #Get [[R,G,B], Width, Height]
    for item in range(len(bubArr)-1,0,-1):
        #Get [R,G,B], Width, Height
        for r,g,b in range(item):
            print(str(r))
            print(str(g))
            print(str(b))
            if bubArr[i]>= bubArr[i+1]:
                temp = bubArr[i]
                bubArr[i] = bubArr[i+1]
                bubArr[i+1] = temp
            
    print("Bubble: \n" + str(bubArr))
    print("")
    return True

def get_colors(sort_me):
    for item in sort_me:
        color = item[0]
        
        
    #for x in range(0, WIDTH):
        #for y in range(0, HEIGHT):

    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        sort_me = change_screen(make_color_list())
        clock.tick(60)
        #to view array - DO NOT RUN on window larger than 50X50
        #print(sort_me)
        #This is where my sorts would go
        #IF I HAD THEM
        get_single_color = get_colors(sort_me)
        #am_i_done = bubble_sort(sort_me)
        

        
    
if __name__ == "__main__":
    main()

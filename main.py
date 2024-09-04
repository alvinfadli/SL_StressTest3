import pygame
import math
import argparse

#flags setup for setting how many pattern to be draw
parser = argparse.ArgumentParser()

parser.add_argument("-total", "--total", help="Total pattern", type=int)

args = parser.parse_args()

print( "Total {} ".format(
        args.total
        ))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

w, h = pygame.display.get_surface().get_size()

def drawPattern(total):
    start_pos_x = 0
    start_pos_y = 0

    end_pos_x = 0
    end_pos_y = 0

    circle_pos_x = 0
    circle_pos_y = 0

    pattern_total =  int(total)

    #first retangle
    pygame.draw.line(screen, "purple", (start_pos_x, start_pos_y), (end_pos_x+w, end_pos_y))
    pygame.draw.line(screen, "purple", (start_pos_x+w, start_pos_y), (end_pos_x+w, end_pos_y+w))
    pygame.draw.line(screen, "purple", (start_pos_x+w,start_pos_y+w), (end_pos_x,end_pos_y+w))
    pygame.draw.line(screen, "purple", (start_pos_x,start_pos_y+w), (end_pos_x, end_pos_y))

    pygame.draw.circle(screen, "purple", ((circle_pos_x+w)/2, (circle_pos_y+w)/2), w/2, width=1)


    pattern_drawed = 0
    radius = w / 2
    innerRectangle_start_pos_x = 0
    innerRectangle_start_pos_y = 0
    innerRectangle_pos_end = 0
    old_inner = 0

    while(pattern_drawed < pattern_total - 1):
        #calculating the starting position of the inner rectangle
        innerRectangle_start_pos_x += radius + (radius * math.cos(225*(math.pi/180)))
        innerRectangle_start_pos_y += radius + (radius * math.sin(225*(math.pi/180)))

        #calculating the width of the inner rectangle
        innerRectangle_pos_end = radius + (radius * math.sin(45*(math.pi/180)))
        innerRectangle_size = innerRectangle_pos_end - innerRectangle_start_pos_x + old_inner

        pygame.draw.rect(screen, "purple", pygame.Rect(innerRectangle_start_pos_x,innerRectangle_start_pos_y, innerRectangle_size, innerRectangle_size), width=1)

        pygame.draw.circle(screen, "purple", ((circle_pos_x+w)/2, (circle_pos_y+w)/2), innerRectangle_size/2, width=1)
        
        radius = innerRectangle_size/2

        #making sure the inner rectange size is same as the circle diameter
        old_inner = innerRectangle_start_pos_x

        pattern_drawed +=1

#running window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    drawPattern(args.total)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
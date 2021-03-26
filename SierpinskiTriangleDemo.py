import pygame, sys
from pygame.locals import *
from tkinter import * 
from math import *
from time import sleep
from numpy.core.defchararray import lower
import random
import keyboard

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

root = Tk()
root.withdraw()
window_width = root.winfo_screenwidth()-100
window_height = root.winfo_screenheight()-100
point_thickness = 3
display_surf = pygame.display.set_mode((window_width,window_height))

#Main Function
def main():
    pygame.init()
    global display_surf
    display_surf = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('Sierpinski\'s Triangle')
    display_surf.fill(BLACK)

offset = 60

length = (window_height-2*offset)/(sin(pi/3))

def findRand():
    rand_x = random.uniform(left[0],right[0])
    rand_y = random.uniform(offset,left[1])
    rand_point = (rand_x,rand_y)
    while(degree(left,rand_point) > pi/3 or degree(right,rand_point) < 2*pi/3or degree(right,rand_point) > pi):
        print("bad")
        rand_x = random.uniform(left[0],right[0])
        rand_y = random.uniform(offset,left[1])
        rand_point = (rand_x,rand_y)
    return rand_point

def degree(p1, p2):
    ydist = -1*(p2[1]-p1[1])
    xdist = p2[0]-p1[0]
    # print(xdist)
    # print(ydist)
    ang = atan2(ydist,xdist)
    print(ang* 180/pi)
    return ang

# print("")
# leftCenterDegree = degree(left,center)
# leftDegree = degree(left,rand_point)
# print("")
# rightCenterDegree = degree(right,center)
# rightDegree = degree(right,rand_point)
# print("")

# print(leftDegree > pi/3)
# print(rightDegree < 2*pi/3)
# print(rightDegree > pi)

def draw(p1, color):
    pygame.draw.circle(display_surf, color , p1, 1, 1)

def isQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def reset():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def move(point):
    pivot = random.randint(1,3)
    if(pivot == 1):
        newx = (center[0] + point[0])/2
        newy = (center[1] + point[1])/2
        color = RED
    elif(pivot == 2):
        newx = (left[0] + point[0])/2
        newy = (left[1] + point[1])/2
        color = BLUE
    else:
        newx = (right[0] + point[0])/2
        newy = (right[1] + point[1])/2
        color = GREEN
    new_point = (newx,newy)
    return (new_point,color)
    


display_surf.fill(BLACK)

center = (window_width/2, offset)
left = (window_width/2-length*cos(pi/3),offset + length*sin(pi/3))
right = (window_width/2+length*cos(pi/3),offset + length*sin(pi/3))

point = findRand()

#Main Loop
while True: 
    isQuit()
    draw(center, RED)   
    draw(left, BLUE)
    draw(right, GREEN)
    new_point = move(point)
    point = new_point[0]
    color = new_point[1]
    draw(point,color)
    pygame.display.flip()
    if keyboard.is_pressed('r'):
        display_surf.fill(BLACK)
        point = findRand()
  
    

if __name__=='__main__':
    main()

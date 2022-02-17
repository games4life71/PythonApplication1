from http import server
from multiprocessing import Event
from pygame.locals import *
import black
import pygame
import random

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode((1000, 700))
running = True #The game is running 
screen.fill(white)
points = [(1,2) , (2,1)]
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and  event.type  == MOUSEMOTION:
            points.append(event.pos)


  
        


    pygame.display.update()
    pygame.draw.lines(screen , green, False , points , 1)


pygame.quit()


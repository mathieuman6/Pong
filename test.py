#!/usr/bin/env python2
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)

    DISPLAY.fill(WHITE)


    pygame.draw.rect(DISPLAY,blue,(0,0,500,2))
    pygame.draw.rect(DISPLAY,blue,(0,398,500,400))
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()


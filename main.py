#Draw Function Assignment
#pip install pygame

import pygame
import sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw")

black = (0, 0, 0)
white = ( 255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

def drawStickman(color, x, y, size):
    pygame.draw.circle(screen, color, (x, y - (size * 20)), size * 4)  # Head
    pygame.draw.line(screen, color, (x, y), (x, y - (size * 20)), size) # Head to Body
    pygame.draw.line(screen, color, (x, y), (x - (size * 4), y + (size * 20)), size)  # Body and left leg
    pygame.draw.line(screen, color, (x, y), (x + (size * 4), y + (size * 20)), size)  # Body and right leg
    pygame.draw.line(screen, color, (x, y), (x - (size * 8), y - (size * 4)), size)  # Body and left arm
    pygame.draw.line(screen, color, (x, y), (x + (size * 8), y - (size * 4)), size)  # Body and right arm

# Game loop
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw stickman
    screen.fill(white)
    drawStickman("green", 400, 300, 5) # Stickman color, X & Y coordinates, and size

    # Update display
    pygame.display.flip()

# Quit the game
pygame.quit()

    #pygame.draw.line(screen, color, (x, y + (y / 6)), (x, y - (y / 6)), size) # Body to Head
    #pygame.draw.line(screen, color, (x, y + (y / 6)), (x - (x / 20), y + (y / 3)), size)  # Body and left leg
    #pygame.draw.line(screen, color, (x, y + (y / 6)), (x + (x / 20), y + (y / 3)), size)  # Body and right leg
    #pygame.draw.line(screen, color, (x, y + (y / 15)), (x - (x / 10), y), size)  # Body and left arm
    #pygame.draw.line(screen, color, (x, y + (y / 15)), (x + (x / 10), y), size)  # Body and right arm
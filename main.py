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
    pygame.draw.circle(screen, color, (x, y - (size * 10)), size * 4)  # Head
    pygame.draw.line(screen, color, (x, y + (size * 6)), (x, y - (size * 10)), size) # Head to Body
    pygame.draw.line(screen, color, (x, y + (size * 6)), (x - (size * 4), y + (size * 20)), size)  # Body and left leg
    pygame.draw.line(screen, color, (x, y + (size * 6)), (x + (size * 4), y + (size * 20)), size)  # Body and right leg
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
    drawStickman("black", 400, 300, 10) # Stickman color, X & Y coordinates, and size
    drawStickman("green", 600, 200, 5)
    drawStickman("red", 200, 200, 5)


    # Update display
    pygame.display.flip()

# Quit the game
pygame.quit()


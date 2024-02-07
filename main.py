#Draw Function Assignment
#pip install pygame

import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw")

BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Stickman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #   self.vx = 0
    #   self.vy = 0
    #   self.speed = 5

    # Draw Function
    def drawStickman():
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 20)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 20), (self.x, self.y + 50), 3)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 30), (self.x - 10, self.y + 20), 3)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 30), (self.x + 10, self.y + 20), 3)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 50), (self.x - 10, self.y + 70), 3)
        pygame.draw.line(screen, BLACK, (self.x, self.y + 50), (self.x + 10, self.y + 70), 3)
        

        #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        #pygame.draw.rect(screen, RED, [55, 50, 20, 25],2)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Main Program Loop 
while not done:
    # Main Event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Drawing
    screen.fill(WHITE)
    drawStickman("RED", 100, 100)

    pygame.display.flip()

    clock.tick(60) # Limited to 60 fps

# Close the window and quit
pygame.quit()
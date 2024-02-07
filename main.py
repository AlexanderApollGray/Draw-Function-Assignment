#Draw Function Assignment
#pip install pygame

import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Draw")

WHITE = ( 255, 255, 255)

# Draw Function
def drawRect():
    pygame.draw.rect(Surface, color, Rect, width=0): return Rect

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

    pygame.display.flip()

    clock.tick(60) # Limited to 60 fps

# Close the window and quit
pygame.quit()
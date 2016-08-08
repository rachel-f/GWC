"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = (16, 135, 94)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

xcoor = 0
ycoor = 0
xspeed = random.randint(-10, 10)
yspeed = random.randint(-10, 10)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND)

    # --- Drawing code should go here

#the ball
    pygame.draw.circle(screen , (135, 16, 45), (xcoor , ycoor ), 20)
    

    if xcoor > 500:
        xspeed = -1
    elif xcoor < 0:
        xspeed = 1
    if ycoor > 700:
        yspeed = -1
    elif ycoor < 0:
        yspeed = 1

    xcoor += xspeed
    ycoor += xspeed

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

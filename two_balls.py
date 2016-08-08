

#importing pygame anda random functions
import pygame
import random

pygame.init()
BACKGROUND = (16, 135, 94)

#size of the screen & setting it as a funciton
size = (700, 500)
screen = pygame.display.set_mode(size)

#how fast the screeen updates
clock = pygame.time.Clock()

#defining varibles for speed & cordinates 
xcoor1 = 0
ycoor1 = 0
xcoor2 = 0
ycoor2 = 0

xspeed1 = random.randint(-10, 10)
yspeed1 = random.randint(-10, 10)
xspeed2 = random.randint(-10, 10)
yspeed2 = random.randint(-10, 10)

done = False
#Main event loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            # background image.
    screen.fill(BACKGROUND)
    #the first ball
    ball_one = pygame.draw.circle(screen , (135, 16, 45), (xcoor1 , ycoor1 ), 20)
    ball_two = pygame.draw.circle(screen , (45, 16, 135), ( xcoor2 + 7 , ycoor2 + 7), 20)

    #if statemnt for staying in the screen first ball
    if xcoor1 > 485:
        xspeed1 = -10
    elif xcoor1 < 0:
        xspeed1 = 10
    if ycoor1 > 685:
        yspeed1 = -10
    elif ycoor1 < 0:
        yspeed1 = 10

 #if statemnt for staying in the screen second ball
    if xcoor2 > 485:
        xspeed2 = -20
    elif xcoor2 < 0:
        xspeed2 = 20
    if ycoor2 > 685:
        yspeed2 = -20
    elif ycoor2 < 0:
        yspeed2 = 20




    xcoor1 += xspeed1
    ycoor1 += xspeed1


    xcoor2 += xspeed2
    ycoor2 += xspeed2

    #updating the screen
    pygame.display.flip()

clock.tick(100)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
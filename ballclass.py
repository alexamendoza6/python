"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
 



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Fish Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()




# BOUNCING BALL CLASS CODE  

class Fish():

    # CONSTRUCTOR METHOD 
    def __init__(self,x_location, y_location, x_speed, y_speed, name):
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed  
        self.name=name


    # # BALL METHODS 
    # def swim(self, screen, color, SCREEN_WIDTH, SCREEN_HEIGHT)

    #     x_location += x_speed
       



    #     pygame.draw.circle(screen, color,x_location,y_location)


fish1= Fish(250,200,5,5,"alexa")


# -------- Main Program Loop -----------
while not done:


    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    


    screen.fill(BLUE)
    # alexa.swim(SCREEN_WIDTH, SCREEN_HEIGHT)
    

    pygame.display.flip()

    
    clock.tick(60)

pygame.quit()
exit() 


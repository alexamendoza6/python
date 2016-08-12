import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

random_colors= [RED, BLUE, GREEN, WHITE, BLACK]

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")


class Snowflake():
	
	def __init__(self, size, position, wind=False):
		self.size = size
		self.position = position
		self.wind = wind
		
	
	def fall(self, speed):
		new_y = self.position[1] + speed 

		if self.wind == True:
			new_x = self.position [0] + random.randint(0, 10)
		else:	
			new_x = self.position [0]

		new_position = [new_x, new_y]
		self.position = new_position
		
		
	def draw(self):
		
		pygame.draw.circle(screen, random.choice(random_colors), self.position, self.size)
		

done = False
clock = pygame.time.Clock()
speed = 1


snow_list = []
	
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	my_snowflake= Snowflake(4, (random.randint(1, 1000),0))

	snow_list.append(my_snowflake)

	screen.fill(BLACK)

	for item in snow_list:
		item.draw()
		item.fall(2)



	pygame.display.flip()
	clock.tick(60)

pygame.quit()
exit() 

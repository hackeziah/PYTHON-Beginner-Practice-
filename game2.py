import pygame

display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pygame.init()


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Race")
clock = pygame.time.Clock()

carIMG = pygame.image.load('car.png')

def car(x,y):
	gameDisplay.blit(carIMG,(x,y))

x = (display_width * 0.4)
y = (display_height * 0.5)


crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		print(event)
	gameDisplay.fill(WHITE)
	car(x,y)
	pygame.display.update()
	clock.tick(60)




pygame.quit()
exit()
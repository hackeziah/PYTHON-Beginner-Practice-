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
x_change= 0
crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0
		print(event)
	x += x_change
	gameDisplay.fill(WHITE)
	car(x,y)
	pygame.display.update()
	clock.tick(60)




pygame.quit()
exit()
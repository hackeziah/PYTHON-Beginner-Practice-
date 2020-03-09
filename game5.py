import pygame
import time
import random

display_width = 800
display_height = 600
car_width = 181
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

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
	textSurface = font.render(text,True,BLACK)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text,largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(5)
	game_loop()

def crash():
	message_display('You Crashed')


def game_loop():
	x = (display_width * 0.4)
	y = (display_height * 0.5)
	x_change= 0

	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 10
	thing_width = 100
	thing_height = 100

	gameExit = False


	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
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
		things(thing_startx,thing_starty,thing_width,thing_height,BLACK)
		thing_starty += thing_speed
		car(x,y)

		if x > display_width - car_width or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)

		if (thing_starty + thing_height) > y:
			if (x > thing_startx and x < thing_startx + thing_width) or (x + car_width > thing_startx and x + car_width < thing_startx + thing_width):
				crash()

		pygame.display.update()
		clock.tick(60)



game_loop()
pygame.quit()
exit()
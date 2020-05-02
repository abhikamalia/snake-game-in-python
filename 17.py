import pygame
import time
import random
pygame.init()

white = (255 , 255 ,255)
black = (0 , 0 , 0)
red = (255 , 0 , 0)
blue = (0 , 0 , 255)
green = (0 , 255 , 0)

display_width = 800
display_height = 600
bolder_x = 200
bolder_y = 200
bolder_width = 20
bolder_height = 100
block_size = 10



FPS = 15

gameDisplay = pygame.display.set_mode((display_width , display_height))




clock = pygame.time.Clock()

font = pygame.font.SysFont(None , 25)
def message_to_screen(msg , color):
	screen_text = font.render(msg , True , color)
	gameDisplay.blit(screen_text , [200 , 200])

def snake(block_size , snakeList):
	for coordinates in snakeList:
		pygame.draw.rect(gameDisplay , black , [coordinates[0] , coordinates[1] , block_size , block_size])

def gameLoop():

	gameExit = False
	gameOver = False
	lead_x = display_width / 2
	lead_y = display_height / 2
	lead_x_change = 0
	lead_y_change = 0
	snakeList = []
	snakeLength = 1

	food_x = round(random.randrange(0 , display_width - block_size)/10.0)*10.0
	food_y = round(random.randrange(0 , display_height - block_size)/10.0)*10.0
	while not gameExit:
		

		while gameOver:
			gameDisplay.fill(white)
			message_to_screen('Game Over , Press C to continue or Q to quit' , red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						gameLoop()
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0



		if lead_x >= display_width:
			lead_x = 0
		if lead_x < 0:
			lead_x = display_width
		if lead_y >= display_height:
			lead_y = 0
		if lead_y < 0:
			lead_y = display_height


		if (lead_x >= bolder_x and lead_x <= bolder_x + bolder_width - 10) and (lead_y >= bolder_y and lead_y <= bolder_y + bolder_height - 10 ):
			gameOver = True

		if lead_x == food_x and lead_y == food_y:
			food_x = round(random.randrange(0 , display_width - block_size)/10.0)*10.0
			food_y = round(random.randrange(0 , display_height - block_size)/10.0)*10.0
			snakeLength += 1
			pygame.display.update()


		for i in snakeList[:-1]:
			if i == snakeHead:
				message_to_screen('Snake bit itself' , red)
				gameOver = True
				pygame.display.update()

		lead_x += lead_x_change
		lead_y += lead_y_change
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay , red , [food_x , food_y , block_size , block_size])

		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		
		if len(snakeList) > snakeLength:
			del snakeList[0]

		snake(block_size , snakeList)
		
		pygame.draw.rect(gameDisplay , blue , [bolder_x , bolder_y , bolder_width , bolder_height])
		pygame.display.update()
		clock.tick(FPS)

	
	pygame.quit()
	quit()


gameLoop()
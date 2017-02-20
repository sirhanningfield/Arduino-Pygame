import pygame 
import serial
import sys , time


comport = 'COM5' #Arduino comport
b_rate = 9600 #arduino bauderate
arduino = serial.Serial(comport,b_rate,timeout=0) #setting the arduino to the serial port
 
WIDTH = 400 # width of the pygame window
HEIGHT = 200 # height of the pygame window

# defining the colors to be used in the game window
WHIGHT = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)


#setting up the gamme display:
game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob")


clock = pygame.time.Clock() # defining the clock method to set frame rate


# Making a ball class to represent the ball. This takes in an argument - color
class Ball : 

	def __init__(self,color):
		self.x = 40
		self.y = 80
		self.size = 10
		self.color = color
		
#defining a class wall to represent wall
class wall:

	def __init__(self,color):

		self.x = 300
		self.y = 30
		self.w = 20
		self.h = 100
		self.color = color
	
# Drawing the game environment:
def draw_environment(ball,wall):
	game_display.fill(WHIGHT)
	pygame.draw.circle(game_display,ball.color,[ball.x,ball.y],ball.size)
	pygame.draw.rect(game_display,wall.color,[wall.x,wall.y,wall.w,wall.h])
	


# Defining the main fuction . This is the function that runs
# and calls all the other classes and fucntions 
def main():
	red_ball = Ball(color = RED) # initializing a red ball 
	green_wall = wall(color = BLUE) #initializing a blue wall

	while True:

		if (arduino.inWaiting()>0):
			time.sleep(0.016)
			pos = arduino.readline().rstrip().decode()
	
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			draw_environment(red_ball,green_wall)
			pygame.display.update()
			
			pos1 = int(pos)
			red_ball.x = pos1
			
			clock.tick(100)



if __name__ == '__main__':
	main()
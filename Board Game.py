
import pygame
import random

#A simulation of a board game is created

#sets a window
surface = pygame.display.set_mode((700,600))
white = (250,250,250)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
brown = (165,42,42)
surface.fill(white)


#Draws grid
for x in range(0,700,100):
	for y in range(0,600,100):
		pygame.draw.line(surface, black, (x,y), (x,y+100))
		pygame.draw.line(surface, black, (x,y), (x+100,y))
#Draws ladder connection at (450,450)
pygame.draw.line(surface, brown, (425,450), (425,250))
pygame.draw.line(surface, brown, (475,450), (475,250))
pygame.draw.line(surface, brown, (425,350), (475,350))
pygame.draw.line(surface, brown, (425,425), (475,425))
pygame.draw.line(surface, brown, (425,290), (475,290))

#Draws ladder connection at (50,250)
pygame.draw.line(surface, brown, (25,250), (25,150))
pygame.draw.line(surface, brown, (75,250), (75,150))
pygame.draw.line(surface, brown, (25,225), (75,225))
pygame.draw.line(surface, brown, (25,175), (75,175))





pygame.display.update()
pygame.time.delay(1000)

current_player = 1

x = -50
y = 550
a = -50
b = 550
pos_1 = (-50,550)
pos_2 = (-50,550)
while True:
	#For player 1
	if current_player == 1:
		pygame.draw.circle(surface,white,(pos_1),45) #erases previous step
		#redraws ladder connection at (50,250)
		pygame.draw.line(surface, brown, (25,250), (25,150))
		pygame.draw.line(surface, brown, (75,250), (75,150))
		pygame.draw.line(surface, brown, (25,225), (75,225))
		pygame.draw.line(surface, brown, (25,175), (75,175))
		#re-draws ladder connection at (450,450)
		pygame.draw.line(surface, brown, (425,450), (425,250))
		pygame.draw.line(surface, brown, (475,450), (475,250))
		pygame.draw.line(surface, brown, (425,350), (475,350))
		pygame.draw.line(surface, brown, (425,425), (475,425))
		pygame.draw.line(surface, brown, (425,290), (475,290))
		#Rolling the dice and determining how many steps to take
		steps = random.randint(1,10)
		#Prints what number is rolled
		print(f'Dice Player 1: {steps}')
		x += steps * 100
		#when x becomes larger than the width, y and x are reset accordingly
		while x > 650: 
			y -= 100
			x -= 700
		pos_1 = (x,y)
		#When player 1 goes where player 2 is player 1 is sent to the beginning
		if pos_1 == pos_2:
			#Player goes to the position where player 2 is and then is sent back to the beginning
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()		
			pygame.time.delay(100)
			pygame.draw.circle(surface,green,(pos_1),45)
			pygame.display.update()	
			x = 50
			y = 550
			pos_1 = (x,y)
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()	
		#When a player is on a certain block they will advance
		if pos_1 == (450,450):
			#Goes to block and then advances
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()		
			pygame.time.delay(100)
			pygame.draw.circle(surface,white,(pos_1),45)
			pygame.display.update()	
			x = 450
			y = 250
			pos_1 = (x,y)
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()	
		elif pos_1 == (50,250):
			#Goes to block then advances
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()
			pygame.time.delay(100)	
			pygame.draw.circle(surface,white,(pos_1),45)
			pygame.display.update()	
			x = 50
			y = 150
			pos_1 = (x,y)
			pygame.draw.circle(surface,red,(pos_1),45)
			pygame.display.update()	
			
		pygame.draw.circle(surface,red,(pos_1),45)
		#Prints the position of the player
		print(f'Player 1: {pos_1}')
		pygame.display.update()
		pygame.time.delay(1000)
	
		if not (pos_1 != (650,50) and y >= 50):
			break
		current_player = 2
	else:
		pygame.draw.circle(surface,white,(pos_2),45)#erases previous step
		#redraws ladder connection at (50,250)
		pygame.draw.line(surface, brown, (25,250), (25,150))
		pygame.draw.line(surface, brown, (75,250), (75,150))
		pygame.draw.line(surface, brown, (25,225), (75,225))
		pygame.draw.line(surface, brown, (25,175), (75,175))
		#re-draws ladder connection at (450,450)
		pygame.draw.line(surface, brown, (425,450), (425,250))
		pygame.draw.line(surface, brown, (475,450), (475,250))
		pygame.draw.line(surface, brown, (425,350), (475,350))
		pygame.draw.line(surface, brown, (425,425), (475,425))
		pygame.draw.line(surface, brown, (425,290), (475,290))
		#Rolling the dice and determining how many steps to take
		steps_two = random.randint(1,10)
		#Prints what number is rolled
		print(f'Dice Player 2: {steps_two}')
		a += steps * 100
		#when x becomes larger than the width, y and x are reset accordingly
		while a > 650:
			b -= 100
			a -= 700
		pos_2 = (a,b)
		#When player 2 goes where player 1 is player 2 is sent to the beginning
		if pos_2 == pos_1:
			#Player goes to the position where player 1 is and then is sent back to the beginning
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()
			pygame.time.delay(100)
			pygame.draw.circle(surface,red,(pos_2),45)
			pygame.display.update()
			a = 50
			b = 550
			pos_2 = (a,b)
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()
		#When a player is on a certain block they will advance
		if pos_2 == (450,450):
			#Goes to block and then advances
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()
			pygame.time.delay(100)
			pygame.draw.circle(surface,white,(pos_2),45)
			pygame.display.update()
			a = 450
			b = 250
			pos_2 = (a,b)
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()	
		elif pos_2 == (50,250):
			#Goes to block and then advances
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()
			pygame.time.delay(100)
			pygame.draw.circle(surface,white,(pos_2),45)
			pygame.display.update()
			a = 50
			b = 150
			pos_2 = (a,b)
			pygame.draw.circle(surface,green,(pos_2),45)
			pygame.display.update()
		pygame.draw.circle(surface,green,(pos_2),45)
		#Prints the position of the player
		print(f'player 2: {pos_2}')
		pygame.display.update()
		pygame.time.delay(1000)
		#Switchs turns between players
		if not (pos_2 != (650,50) and b >= 50):
			break
		current_player = 1
		
		
		


		




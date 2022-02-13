#101245319 Ashneet Nagi
import pygame

#lists for areas
names = ['movie theatre','gallery','study area','rest area','kitchen','dining room','ice rink','game room','cat cafe','sports centre','adventure park','coffee shop','dog park','sitting area','lake','tool shed','soccer field','garden','playground','beach']

#lists for area descriptions 
descriptions = ['A great place to watch movies!Is located inside.', 'Is located inside. Has several Art pieces','Is located inside. A quiet place to study', 'Is located inside. A comfortable place to sleep and rest','Is located inside. Has delicious foods ready to be served!','Is located inside. A great place to eat delicious food','Is located inside. Great place to go skating, and play hockey','Is located inside. Has all the games you can imagine!','Is located inside. A chance to meet adorable cats','Is located inside. Has all the sports gear you need!','Is located outside. A small adventure park that has thrilling rides','Is located outside. Great place to relax and get coffee','Is located outside. A fun place for dogs!','Is located outside. A relaxing sitting are near beside the lake for a great view!','Is located outside. A big lake with a dock to boat.', 'Is located outside. A tool shed for the garden','Is located outside. A field to player soccer in, and other sports.','Is located outside. Has various plants and a beautiful place!','Is located outside. Place for children to play in.','Is located outside. Great place to relax under the sun.']

#lists for items user can add
inventory = []

#lists for directions that align with each area
directions = [['west','south'],['east','west'],['east','west'],['east','south west'],['north','west'],['north','west','east'],['east','west','south'],['east','west','south west'],['north east','east','south'],['north','north east'],['west'],['east','west','south'],['east','west','south'],['north','east','west','south'],['east','south'],['north','west'],['north','east','west'],['north','east','west'],['north','east','south west'],['north east']]

#list for the area locations connected to current area
graph = [[1,4],[0,2],[1,3],[2,8],[0,5],[0,6,4],[5,7,13],[6,8,9],[3,7,9],[8,7],[11],[10,12,15],[11,13,16],[6,12,14,17],[13,18],[11,16],[12,15,17],[13,16,18],[14,17,19],[18]]

#displays map 
img = pygame.image.load('map.JPG')
pygame.transform.rotate(img,90)
img = pygame.transform.scale(img,(700,600))
surface = pygame.display.set_mode((700,600))
surface.blit(img,(0,0))
pygame.display.update()


#starts at a certain location
c_location = 'movie theatre'
while True:
	#displays current location
	index_location = names.index(c_location)
	print(f'\nYour current location is the {c_location}: {descriptions[index_location]}')
	#prints out rooms to exit to from current location
	print('You can exit to:')
	for rooms in graph[index_location]:
		print(f'{directions[index_location][graph[index_location].index(rooms)]} of {c_location} to {names[rooms]}')
		
	
	nxt_location = input('What would you like to do?').lower()
	
	#adds flowers to inventory 
	if nxt_location == 'take' and c_location == 'garden':
		#checks if item is already in inventory
		for i in inventory:
			if i == 'Flowers':
				print('item is already inventory')
				break
				
		else:
			inventory.append('Flowers')
			print('Flowers has been added to inventory!')
			
	#adds poutine to inventory
	elif nxt_location == 'take' and c_location == 'kitchen':
		#checks if item is already in inventory
		for i in inventory:
			if i == 'Poutine':
				print('item is already in inventory')
				break
		else:
			inventory.append('Poutine')
			print('Poutine has been added to inventory!')
	#adds art piece to inventory
	elif nxt_location == 'take' and c_location == 'gallery':
		#checks if item is already in inventory
		for i in inventory:
			if i == 'Art piece':
				print('item is already in inventory')
				break
				
		else:
			inventory.append('Art piece')
			print('An art piece has been added to inventory!')
	#Shows what is inside the inventory
	elif nxt_location == 'inventory':
		print(inventory)
	#gives instructions
	elif nxt_location == 'help':
		print('The program will explain where your current location is and the exits you can take to other areas\nTo go to another area enter the direction of the location relevant to the current location\nAt specific areas you can pick up items and add them to your inventory\nTo do this enter "take"\nenter inventroy to check inventory\nenter quit to quit the program')
	#quits program
	elif nxt_location == 'quit':
		break
	
	else:
		#checks to see if user input is valid to change the location
		for i in directions[index_location]:
			if nxt_location == i:
				no = directions[index_location].index(nxt_location)
				area = graph[index_location][no]
				c_location = names[area]
				break
		#if user input is invalid 
		else:
			print('please try a valid input')
		
		
		


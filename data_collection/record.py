import pygame

width_map=670
height_map=760

white = (255, 255, 255)
red=(255,0,0)
black = (0, 0, 0)
key_1_press=False
downsample=4
def display_default_img():
	# read image file and rescale it to the window size
	introScreenImage = pygame.image.load("./images/SPMSmap_circled.jpg")
	introScreenImage = pygame.transform.scale(introScreenImage, (width_map, height_map))
	screen = pygame.display.set_mode((1100, height_map))
	screen.fill(white)
	screen.blit(introScreenImage, (0, 0))

	#display words
	message_to_screen(screen,"Input your details:", black, 25)
	message_to_screen(screen,"1. Select your position on the map", black, 50)
	message_to_screen(screen,"2. Select your preferences:", black, 75)
	return screen

def message_to_screen(screen,msg, color, y_pos):
	font = pygame.font.Font(None, 30)
	screen_text = font.render(msg, True, color)
	screen.blit(screen_text,(650,y_pos))

## define event handler for mouse click. 
## this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
	finish = False
	global key_1_press
	while finish == False:
	## pygame.event.get() retrieves all events made by user
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finish = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					key_1_press=True
				if event.key == pygame.K_2:
					key_1_press=False
			if key_1_press==True:
				if event.type == pygame.MOUSEMOTION:
					(mouseX, mouseY) = pygame.mouse.get_pos()
					print((mouseX, mouseY))
					finish = True
	return (mouseX, mouseY)


def get_user_location(screen):
	#will update the contents of the entire display window
	pygame.display.flip()
	
	# get outputs of Mouseclick event handler 
	buttonX, buttonY = MouseClick()
	#display_default_img()
	return (buttonX,buttonY)

def verify_click(screen):
	x_coord,y_coord=get_user_location(screen)
	if x_coord >=670:
		print("Wrong location. Please click again")
		return(0,0)
	else:
		pygame.draw.circle(screen,red, (x_coord,y_coord), 2)
#		pygame.draw.line(screen, red, [x_coord-10, y_coord-10], [x_coord+10,y_coord+10], 2)
#		pygame.draw.line(screen, red, [x_coord+10, y_coord-10], [x_coord-10,y_coord+10], 2)
		return(x_coord,y_coord)
pygame.init()
pygame.display.set_caption("Canteen")
screen=display_default_img()
x_save=0
y_coord=0
while True:
	x_coord,y_coord=verify_click(screen)
	if x_coord==0 and y_coord==0:
		continue
	if x_coord//downsample!=x_save or y_coord//downsample!=y_save:

		text_file = open("obstacle.txt", "a")
		text_file.write("("+str(x_coord//downsample)+","+str(y_coord//downsample)+")"+",")
	x_save=x_coord//downsample
	y_save=y_coord//downsample
	print((x_coord , x_coord))

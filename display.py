import pygame
import time
import numpy as np
from menu_data import menu_data

white = (255, 255, 255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black = (0, 0, 0)

class pg_display:

	def __init__(self,text=''):
		self.text = text
		self.width_map=670
		self.height_map=760
		self.active = False
		self.map_coord_status=False
		self.screen = None
		self.display_stage=0
		self.x_coord=0
		self.y_coord=0
		self.text_rect0 = pygame.Rect(720, 300, 140, 32)
		self.color= pygame.Color('lightskyblue3')
		self.font = pygame.font.Font('./fonts/Calibri.ttf', 25)

	def display_welcome_img(self):
		clock = pygame.time.Clock()
		t1=time.time()
		t2=10
		self.screen = pygame.display.set_mode((1100, self.height_map))
		self.screen.fill(black)

		ntu_logo = pygame.image.load("./images/ntu_logo.png").convert_alpha()
		ntu_logo = pygame.transform.scale(ntu_logo, (377, 134))
		ntu_surf = ntu_logo.copy()
		alpha_ntu_surf = pygame.Surface(ntu_surf.get_size(), pygame.SRCALPHA)

		font = pygame.font.Font('./fonts/Calibri.ttf', 64)
		orig_surf= font.render('NTU F&B Recommendation', True, (0,255,239))
		txt_surf = orig_surf.copy()
		alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
		alpha = 255
		while (t2-t1)<=2.5:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
			if alpha > 0:
				# Reduce alpha each frame, but make sure it doesn't get below 0.
				alpha = max(0, alpha-4)
				# Create a copy so that the original surface doesn't get modified.
				txt_surf = orig_surf.copy()
				ntu_surf = ntu_logo.copy()
				alpha_surf.fill((255, 255, 255, alpha))
				alpha_ntu_surf.fill((255, 255, 255, alpha))
				txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
				ntu_surf.blit(alpha_ntu_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

			self.screen.fill(black)
			self.screen.blit(ntu_surf,(360,280))
			self.screen.blit(txt_surf, (200, 420))
			pygame.display.flip()
			clock.tick(33)
			t2=time.time()
		self.display_default_img()

	def display_default_img(self):
		# read image file and rescale it to the window size
		NTU_map = pygame.image.load("./images/SPMSmap_circled.jpg")
		NTU_map = pygame.transform.scale(NTU_map, (self.width_map, self.height_map))
		self.screen = pygame.display.set_mode((1100, self.height_map))
		self.screen.fill(black)
		self.screen.blit(NTU_map, (0, 0))

		#display words
		self.font = pygame.font.Font('./fonts/Calibri.ttf', 25)
		self.message_to_screen("Input your details:", white,700, 30)
		self.message_to_screen("1. Select your position on the map", white,700,80)
		self.message_to_screen("2. Select your preferences:", white,700,130)
		pygame.draw.rect(self.screen,red,(720, 170,300, 60))
		self.message_to_screen("Type of Cuisine", white,800,190)
		self.message_to_screen("3. Price range:", white,700,260)
		self.message_to_screen(self.text, white,725, 305)
		# Blit the rect.
		pygame.draw.rect(self.screen, self.color, self.text_rect0, 2)

	def draw_route(self,coords):
		for coord in coords:
			pygame.draw.circle(self.screen,red, (coord[0],coord[1]), 3)
			pygame.display.flip()

	def route_text_message(self,wait=True):
		if wait==True:
			self.message_to_screen("Calculating route ...", white,700,600)
		else:
			pygame.draw.line(self.screen, blue, [self.x_coord-10, self.y_coord-10], [self.x_coord+10,self.y_coord+10], 5)
			pygame.draw.line(self.screen, blue, [self.x_coord+10, self.y_coord-10], [self.x_coord-10,self.y_coord+10], 5)
			self.message_to_screen("Shortest route shown on the map!", white,700,600)

	def display_cuisine_img(self):

		cuisine=menu_data.cuisine_placeholders()
		self.screen = pygame.display.set_mode((1050, 580))
		self.font = pygame.font.Font('./fonts/Calibri.ttf', 30)
		self.message_to_screen("Choose Your Cuisine", white,405,30)

		self.load_img(cuisine[0],(250,200),(10,80),alpha=True)
		self.message_to_screen("Western", white,88,170)

		self.load_img(cuisine[1],(250,200),(270,290),alpha=True)
		self.message_to_screen("Chinese", white,340,375)

		self.load_img(cuisine[2],(250,200),(10,290),alpha=True)
		self.message_to_screen("Korean", white,90,375)

		self.load_img(cuisine[3],(250,200),(270,80),alpha=True)
		self.message_to_screen("Japanese", white,340,170)

		self.load_img(cuisine[4],(250,200),(530,80),alpha=True)
		self.message_to_screen("Malay", white,620,170)

		self.load_img(cuisine[5],(250,200),(530,290),alpha=True)
		self.message_to_screen("Indian", white,620,375)

		self.load_img(cuisine[6],(250,200),(790,80),alpha=True)
		self.message_to_screen("Thai", white,883,170)

		self.load_img(cuisine[7],(250,200),(790,290),alpha=True)
		self.message_to_screen("Drinks", white,875,375)

		self.load_img(menu_data.BackBut,(70,70),(490,500))

		pygame.display.flip()

	def display_menu_img(self):

		if self.display_stage==2.1:
			a=0

		elif self.display_stage==2.2:
			a=1

		elif self.display_stage==2.3:
			a=2

		elif self.display_stage==2.4:
			a=3

		elif self.display_stage==2.5:
			a=4

		elif self.display_stage==2.6:
			a=5

		elif self.display_stage==2.7:
			a=6
		menu = menu_data.menu_placeholders

		self.screen=pygame.display.set_mode((1050, 580))
		self.message_to_screen("Select from the menu", white,420,30)
		self.load_img(menu[a][0],(250,200),(10,80))
		self.load_img(menu[a][1],(250,200),(270,290))
		self.load_img(menu[a][2],(250,200),(10,290))
		self.load_img(menu[a][3],(250,200),(270,80))
		self.load_img(menu[a][4],(250,200),(530,80))
		self.load_img(menu[a][5],(250,200),(530,290))
		self.load_img(menu[a][6],(250,200),(790,80))
		self.load_img(menu_data.BackBut,(70,70),(490,500))

		pygame.display.flip()

	def message_to_screen(self,msg, color,x_pos, y_pos):
		screen_text = self.font.render(msg, True, color)
		self.screen.blit(screen_text,(x_pos,y_pos))

	def load_img(self,menu,img_scale,img_coord,alpha=False):
		load_picture=pygame.image.load(menu)
		picture= pygame.transform.scale(load_picture, img_scale)
		if alpha==True:
			picture.set_alpha(120)
		self.screen.blit(picture, img_coord)

	## define event handler for mouse click. 
	## this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
	def MouseClick(self):
		finish = False
		while finish == False:
		## pygame.event.get() retrieves all events made by user
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					finish = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					(mouseX, mouseY) = pygame.mouse.get_pos()
					finish = True
					# If the user clicked on the input_box rect.
					if self.text_rect0.collidepoint(event.pos):
						# Toggle the active variable.
						self.active = not self.active
					else:
						self.active = False
					self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')

				if event.type == pygame.KEYDOWN:
					if self.active:
						if event.key == pygame.K_RETURN:
							self.text = ''
						elif event.key == pygame.K_BACKSPACE:
							self.text = self.text[:-1]
						else:
							self.text += event.unicode
						print (self.text)

						# Re-render the text.)
						self.display_default_img()
			#will update the contents of the entire display window
			pygame.display.flip()
		return (mouseX, mouseY)


	'''
	check the self.display_stage and choose the relevant option
	'''
	def get_user_location(self):

		self.x_coord,self.y_coord=self.MouseClick()
		self.map_coord_status=False
		if self.display_stage==0:
			self.check_stage0_option()
			return(self.x_coord,self.y_coord,self.map_coord_status)
		if self.display_stage==1:
			self.check_stage1_option()
			return(self.x_coord,self.y_coord,self.map_coord_status)

	'''
	check the mouse poistion of the main display
	'''

	def check_stage0_option(self):

		if self.x_coord <=640:
			self.display_stage=0
			self.display_default_img()

			pygame.draw.line(self.screen, blue, [self.x_coord-10, self.y_coord-10], [self.x_coord+10,self.y_coord+10], 5)
			pygame.draw.line(self.screen, blue, [self.x_coord+10, self.y_coord-10], [self.x_coord-10,self.y_coord+10], 5)
			self.map_coord_status=True

		else:
			#Type of cuisine
			self.box_clicked(720,1020,170,230,1)

	'''
	check the mouse poistion of the cusine display
	'''
	def check_stage1_option(self):
		#western
		self.box_clicked(10,260,80,280,2.1)

		#korean
		self.box_clicked(10,260,290,490,2.2)

		#Jap
		self.box_clicked(270,520,80,280,2.3)

		#Chinese
		self.box_clicked(270,520,290,490,2.4)

		#Malay
		self.box_clicked(530,780,80,280,2.5)

		#Indian
		self.box_clicked(530,780,290,490,2.6)

		#Thai
		self.box_clicked(790,1040,80,280,2.7)

		#Drinks
		self.box_clicked(790,1040,290,490,2.8)

		#back button
		self.box_clicked(490,560,500,570,0)

	def box_clicked(self,x_min,x_max,y_min,y_max,display_stage):
		if self.x_coord>x_min and self.x_coord<x_max and self.y_coord>y_min and self.y_coord<y_max:
			self.display_stage=display_stage
			if display_stage ==0:
				self.display_default_img()
			elif display_stage ==1:
				self.display_cuisine_img()
			elif display_stage >=2 or display_stage <=3:
				self.display_menu_img()

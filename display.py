import pygame
import numpy as np
from menu_data import menu_data

black = (0, 0, 0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
forestgreen=(34,139,34)
darkgreen=(0,100,0)
Cadet_Blue=(95,158,160)
purple=(75,0,130)
pink=(255,105,180)
orange=(249,166,2)
white = (255, 255, 255)

class pg_display:

	def __init__(self,text=''):
		self.text0 = text
		self.text1 = text
		self.otxt0 = text
		self.otxt1 = text
		self.text0_saved = text +" "
		self.text1_saved = text +" "
		self.saved_recommend= text
		self.userprice_range=[-1]
		self.width_map=670
		self.height_map=760
		self.active0 = False
		self.active1 = False
		self.map_coord_status=False
		self.screen = None
		self.display_stage=0
		self.food_selected=0
		self.x_coord=0
		self.y_coord=0
		self.x_coord_map=0
		self.y_coord_map=0
		self.shortest_coords=[]
		self.text_rect0 = pygame.Rect(750, 300, 140, 32)
		self.text_rect1 = pygame.Rect(935, 300, 140, 32)
		self.output_box0 = pygame.Rect(750, 350, 140, 32)
		self.output_box1 = pygame.Rect(935, 350, 140, 32)
		self.color_lb = pygame.Color('lightskyblue3')
		self.color_db = pygame.Color('dodgerblue2')
		self.color0= pygame.Color('lightskyblue3')
		self.color1= pygame.Color('lightskyblue3')
		self.font = pygame.font.Font('./fonts/Calibri.ttf', 25)

	def display_welcome_img(self):
		clock = pygame.time.Clock()
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
		alpha = 0
		while alpha !=255:
			# Reduce alpha each frame, but make sure it doesn't get below 0.
			alpha = min(255, alpha+1)
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
			clock.tick(90)
		clock.tick(1)
		self.display_default_img()

	def display_exit_img(self):
		clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((1100, self.height_map))
		self.screen.fill(black)

		font = pygame.font.Font('./fonts/Calibri.ttf', 64)
		orig_surf= font.render('Standing on the shoulders of giants ...', True, (255,255,0))
		txt_surf = orig_surf.copy()
		alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
		alpha = 255

		while alpha !=0:
			# Reduce alpha each frame, but make sure it doesn't get below 0.
			alpha = max(0, alpha-1)
			# Create a copy so that the original surface doesn't get modified.
			txt_surf = orig_surf.copy()
			alpha_surf.fill((255, 255, 255, alpha))
			txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
			self.screen.fill(black)
			self.screen.blit(txt_surf, (60, 360))
			pygame.display.flip()
			clock.tick(100)

	def display_default_img(self):
		# read image file and rescale it to the window size
		NTU_map = "./images/SPMSmap_circled.jpg"
		cuisine_button = "./images/button_type-of-cuisine.png"
		exit_button = "./images/button_exit.png"
		compute_button = "./images/button_compute-recommendation.png"
		self.font = pygame.font.Font('./fonts/Calibri.ttf', 25)
		self.screen = pygame.display.set_mode((1100, self.height_map))
		self.screen.fill(black)

		#load images
		self.load_img(cuisine_button,(300,60),(720,170))
		self.load_img(exit_button,(90,40),(980,690))
		self.load_img(NTU_map,(self.width_map,self.height_map),(0,0))
		self.load_img(compute_button,(373,45),(700,500))

		for i in range(len(self.shortest_coords)):
			for coord in self.shortest_coords[i]:
				if i == 0:
					color=red
				elif i ==1:
					color=darkgreen
				elif i ==2:
					color=blue
				pygame.draw.circle(self.screen,color, (coord[0],coord[1]), 3)

		if self.x_coord_map !=0 and self.y_coord_map !=0:
			pygame.draw.line(self.screen, black, [self.x_coord_map-10, self.y_coord_map-10], [self.x_coord_map+10,self.y_coord_map+10], 5)
			pygame.draw.line(self.screen, black, [self.x_coord_map+10, self.y_coord_map-10], [self.x_coord_map-10,self.y_coord_map+10], 5)

		if self.saved_recommend != "":
			self.message_to_screen("1. "+self.saved_recommend[0], Cadet_Blue ,820, 560)
			self.message_to_screen("2. "+self.saved_recommend[1], forestgreen,820, 590)
			self.message_to_screen("3. "+self.saved_recommend[2], red,820, 620)

		#display words
		self.message_to_screen("Input your details:", white,700, 30)
		self.message_to_screen("1. Select your position on the map", white,700,80)
		self.message_to_screen("2. Select your preferences:", white,700,130)
		self.message_to_screen("3. Price range:", white,700,260)
		self.message_to_screen("S$", white,725,305)
		self.message_to_screen("-", white,898,305)
		self.message_to_screen("S$", white,910,305)
		self.message_to_screen(self.text0, white,755, 305)
		self.message_to_screen(self.text1, white,940, 305)
		# Blit the rect.

		if self.active0 == True:
			self.color0=self.color_db
		elif self.text0_saved ==self.text0:
			self.color0=(0,255,0)
		else:
			self.color0=self.color_lb

		if self.active1 == True:
			self.color1=self.color_db
		elif self.text1_saved ==self.text1:
			self.color1=(0,255,0)
		else:
			self.color1=self.color_lb

		pygame.draw.rect(self.screen, self.color0, self.text_rect0, 2)
		pygame.draw.rect(self.screen, self.color1, self.text_rect1, 2)
		pygame.draw.rect(self.screen,black,self.output_box0,0)
		pygame.draw.rect(self.screen,black,self.output_box1,0)

		self.check_food_select()
		price_range=self.check_price_range()
		self.userprice_range=price_range
		pygame.display.flip()

	def reinitilize_default_img(self):
		self.__init__()
		self.display_default_img()

	def recommended_canteen(self,name):
		self.saved_recommend=name
		self.display_default_img()

	def check_price_range(self):
		try:
			price_range=[float(self.otxt0),float(self.otxt1)]
			if price_range[0]<price_range[1]:
				self.message_to_screen("Entered amount: S$  "+ self.otxt0+" - "+self.otxt1, white,740, 355)
				return price_range
			else:
				self.message_to_screen("Max less than min", white,740, 355)
				return [-1]

		except:
			if self.otxt0!="" and self.otxt1!="":
				self.message_to_screen("Wrong Input entered", white,740, 355)
			return [-1]

	def check_food_select(self):
		if self.food_selected>3:
			pass
			pygame.draw.line(self.screen, green, [812, 212], [837,246], 6)
			pygame.draw.line(self.screen, green, [837, 246], [925,155], 6)

	def draw_route(self,coords):
		self.shortest_coords=[]
		for coord in coords:
			pygame.draw.circle(self.screen,red, (coord[0],coord[1]), 3)
		pygame.display.flip()

	def shortest_route(self,coords,wait=True):
		self.shortest_coords=coords
		self.display_default_img()
		self.route_text_message(wait)

	def route_text_message(self,wait=True):
		if wait==True:
			self.message_to_screen("Calculating route ...", white,700,650)
		else:
			self.message_to_screen("Shortest route shown on the map!", white,700,650)
		pygame.display.flip()

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
		self.message_to_screen("Not available", red,840,400)
		self.load_img(menu_data.PreBut,(125,35),(60,520))

		pygame.display.flip()

	def display_menu_img(self):
		a=int((((self.display_stage-2)*10)+0.5)//1)
		menu = menu_data.menu_placeholders
		self.screen=pygame.display.set_mode((1050, 580))
		self.message_to_screen("Select from the menu", white,420,30)
		self.load_img(menu[a][0],(250,200),(10,80))
		self.load_img(menu[a][1],(250,200),(10,290))
		self.load_img(menu[a][2],(250,200),(270,80))
		self.load_img(menu[a][3],(250,200),(270,290))
		self.load_img(menu[a][4],(250,200),(530,80))
		self.load_img(menu[a][5],(250,200),(530,290))
		self.load_img(menu[a][6],(250,200),(790,80))
		self.load_img(menu_data.MenuBut,(125,35),(870,520))
		self.load_img(menu_data.PreBut,(125,35),(60,520))

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

					if self.display_stage==0:
						# If the user clicked on the input_box rect.
						if self.text_rect0.collidepoint(event.pos):
							# Toggle the active variable.
							self.active0 = not self.active0
						else:
							self.active0 = False

						if self.text_rect1.collidepoint(event.pos):
							self.active1 = not self.active1
						else:
							self.active1 = False
						self.display_default_img()

				if event.type == pygame.KEYDOWN:

					if self.display_stage==0:
						if self.active0:
							if event.key == pygame.K_RETURN:
								self.otxt0 = self.text0
								self.active0 = False
								self.color0 = (0,255,0)
								txt_surface0 = self.font.render(self.otxt0, True, self.color0)
								self.text0_saved =self.text0
							elif event.key == pygame.K_BACKSPACE:
								self.text0 = self.text0[:-1]
							else:
								if len(self.text0)<=9:
									self.text0 += event.unicode


						if self.active1:
							if event.key == pygame.K_RETURN:
								self.otxt1 = self.text1
								self.active1 = False
								self.color1 = (0,255,0)
								txt_surface1 = self.font.render(self.otxt1, True, self.color1)
								self.text1_saved =self.text1
							elif event.key == pygame.K_BACKSPACE:
								self.text1 = self.text1[:-1]
							else:
								if len(self.text1)<=9:
									self.text1 += event.unicode


						# Re-render the text
						self.display_default_img()
		return (mouseX, mouseY)


	'''
	check the self.display_stage and choose the relevant option
	'''
	def get_user_location(self,compute_status=False):
		self.compute_status=compute_status
		self.x_coord,self.y_coord=self.MouseClick()
		self.map_coord_status=False
		if self.display_stage==0:
			self.check_stage0_option()
			return(self.x_coord,self.y_coord,self.map_coord_status,self.userprice_range,self.compute_status,self.food_selected)
		elif self.display_stage==1:
			self.food_selected=0
			self.check_stage1_option()
			return(self.x_coord,self.y_coord,self.map_coord_status,self.userprice_range,self.compute_status,self.food_selected)
		elif self.display_stage>=2 and self.display_stage<3:
			self.check_stage2_option()
			return(self.x_coord,self.y_coord,self.map_coord_status,self.userprice_range,self.compute_status,self.food_selected)


	'''
	check the mouse poistion of the main display
	'''

	def check_stage0_option(self,text=""):
		self.map_coord_status=False
		if self.x_coord <=640:
			self.x_coord_map=self.x_coord
			self.y_coord_map=self.y_coord
			self.display_default_img()
			self.map_coord_status=True

		#compute button
		elif self.x_coord>700 and self.x_coord<1073 and self.y_coord>500 and self.y_coord<545:
			self.compute_status =True

		elif self.x_coord>980 and self.x_coord<1070 and self.y_coord>690 and self.y_coord<730:
			self.display_exit_img()
			pygame.quit()
			exit()

		#Type of cuisine
		elif self.x_coord>720 and self.x_coord<1020 and self.y_coord>170 and self.y_coord<230:
			self.display_stage=1
			self.display_cuisine_img()

	'''
	check the mouse poistion of the cusine display
	'''
	def check_stage1_option(self):

		#western
		self.box_clicked(10,260,80,280,2.0)

		#korean
		self.box_clicked(10,260,290,490,2.1)

		#Jap
		self.box_clicked(270,520,80,280,2.2)

		#Chinese
		self.box_clicked(270,520,290,490,2.3)

		#Malay
		self.box_clicked(530,780,80,280,2.4)

		#Indian
		self.box_clicked(530,780,290,490,2.5)

		#Thai
		self.box_clicked(790,1040,80,280,2.6)

		#Drinks
		#self.box_clicked(790,1040,290,490,2.8)

		#back button
		self.box_clicked(60,185,520,555,0)

	def check_stage2_option(self):
		a=self.display_stage+1

		self.box_clicked(10,260,80,280,a+0.005)
		self.box_clicked(10,260,290,490,a+0.015)
		self.box_clicked(270,520,80,280,a+0.025)
		self.box_clicked(270,520,290,490,a+0.035)
		self.box_clicked(530,780,80,280,a+0.045)
		self.box_clicked(530,780,290,490,a+0.055)
		self.box_clicked(790,1040,80,280,a+0.065)

		self.box_clicked(870,995,520,555,0) #(125,35),(870,520)
		self.box_clicked(60,185,520,555,1)


	def box_clicked(self,x_min,x_max,y_min,y_max,display_stage):
		if self.x_coord>x_min and self.x_coord<x_max and self.y_coord>y_min and self.y_coord<y_max:
			self.display_stage=display_stage
			if display_stage ==0:
				self.display_default_img()
			elif display_stage ==1:
				self.display_cuisine_img()
			elif display_stage >=2 and display_stage <3:
				self.display_menu_img()
			elif display_stage >=3 and display_stage < 4:
				self.food_selected=display_stage
				self.display_stage=0
				self.display_default_img()


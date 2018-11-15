import pygame
import Algo
import Astar
import display
import numpy as np
from route_data import route_data
from menu_data import menu_data

compute_status=False
canteen_route_score_dict={}
canteen_paths_dict={}
price_score_dict={}
food_score_dict={}

pygame.init()
pygame.display.set_caption("Canteen")
pygame_display=display.pg_display()
pygame_display.display_welcome_img()
astar_graph=Astar.AStarGraph(route_data.Obstacles_mtx,route_data.bus_mtx,route_data.bus_stop_mtx)

while True:
	x_now,y_now,map_coord_status,userprice_range,compute_status,food_selected=pygame_display.get_user_location(compute_status)

	'''
	Calculate score based on distance
	'''
	if map_coord_status==True:
		canteens_coords=[]
		canteens_routes_names=[]
		pygame_display.recommended_canteen('')
		for keys in menu_data.canteen_data:
			canteens_coord=menu_data.canteen_data[keys]["can_coord"]
			canteens_coords.append(canteens_coord)
			canteens_routes_names.append(keys)
		route_names,route_reward,route_paths=Algo.sort_distance(x_now,y_now,astar_graph,pygame_display,canteens_coords,canteens_routes_names)

		for i in range(len(route_names)):
			canteen_route_score_dict[route_names[i]]=route_reward[i]
			canteen_paths_dict[route_names[i]]=route_paths[i]
		#print (canteen_route_score_dict)

	if compute_status==True:	#check whether the compute button is clicked

		#Calculate score based on cusine selected
		food_score_dict=Algo.search_by_food(food_selected,food_score_dict)
		#print (food_score_dict)

		#Calculate score based on price range
		price_score_dict=Algo.search_by_price(userprice_range,price_score_dict)
		#print (price_score_dict)

		Algo.sort_by_rank(canteen_route_score_dict,price_score_dict,food_score_dict,canteen_paths_dict,pygame_display)
	compute_status=False

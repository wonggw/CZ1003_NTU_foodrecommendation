import pygame
import Algo
import Astar
import operator
from route_data import route_data
from menu_data import menu_data
import numpy as np
import display

compute_status=False
canteen_route_score_dict={}

pygame.init()
pygame.display.set_caption("Canteen")
pygame_display=display.pg_display()
pygame_display.display_welcome_img()
astar_graph=Astar.AStarGraph(route_data.Obstacles_mtx,route_data.bus_mtx,route_data.bus_stop_mtx)

while True:
	price_score_dict={}
	food_score_dict={}
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
		route_names,route_reward=Algo.distance_a_b(x_now,y_now,astar_graph,pygame_display,canteens_coords,canteens_routes_names)

		for i in range(len(route_names)):
			canteen_route_score_dict[route_names[i]]=route_reward[i]
		#print (canteen_route_score_dict)

	if compute_status==True:	#check whether the compute button is clicked
		price_scores=[]
		canteens_prices_names=[]
		
		'''
		Calculate score based on cusine selected
		'''
		if food_selected !=0:
			a=(int(np.floor((food_selected-3)*10)))
			b=(int(np.floor((((food_selected-3)*10-a)*10))))
			food_selected=menu_data.stores_placeholder[a][b]
			for keys in menu_data.canteen_data:
				for values_1 in menu_data.canteen_data[keys]["can_food"]:
					for food in food_selected:
						if food==values_1:
							food_score_dict[keys]=1
			#print (food_score_dict)

		'''
		Calculate score based on price range
		'''
		if userprice_range !=[-1]:
			pygame_display.reinitilize_default_img()
			prices_overlaps=[]
			price_canteens=[]
			for keys in menu_data.canteen_data:
				prices_overlaps=[]
				for values_2 in menu_data.canteen_data[keys]["can_price"]:
					prices_overlap=Algo.OVL_two_random_arr(values_2,userprice_range,20)
					prices_overlaps.append(prices_overlap)
					#print (prices_overlap,keys)
				#normalize_prices_overlaps=Algo.normalize_meanstd(prices_overlaps)
				price_score=np.sum(prices_overlaps)/len(menu_data.canteen_data[keys]["can_price"])
				price_scores.append(price_score)
				price_canteens.append(keys)
			normalize_price_scores=Algo.normalize_meanstd(price_scores)

			for i in range(len(price_canteens)):
				if np.isnan(normalize_price_scores[i]):
					normalize_price_scores[i]=0
				price_score_dict[price_canteens[i]]=normalize_price_scores[i]
			#print (price_score_dict)
		'''
		Total all the score
		'''
		combined_score_dict={key: canteen_route_score_dict.get(key, 0) + price_score_dict.get(key, 0)/5 + food_score_dict.get(key, 0) for key in set(canteen_route_score_dict) | set(price_score_dict)| set(food_score_dict)}
		print ("Combined score\n",combined_score_dict)
		highest_score=max(combined_score_dict.items(), key=operator.itemgetter(1))[0] #find the canteen with the highest score
		#print (highest_score)
		pygame_display.recommended_canteen(highest_score)
	compute_status=False

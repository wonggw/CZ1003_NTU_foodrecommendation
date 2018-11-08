import numpy as np
import Astar
import display
from route_data import route_data

def normalize_meanstd(a, axis=None): 
	# axis param denotes axes along which mean & std reductions are to be performed
	mean = np.mean(a, axis=axis, keepdims=True)
	std = np.sqrt(((a - mean)**2).mean(axis=axis, keepdims=True))
	return (a - mean) / std

def distance_a_b(x_now,y_now,astar_graph,pygame_display):
	route_costs=[]
	route_paths=[]
	i=0
	pygame_display.route_text_message()
	canteens_coords_downsample=[[a[0]//4, a[1]//4] for a in route_data.canteens_coords] 
	for canteens_coord_downsample in canteens_coords_downsample:
		routes_downsample,cost =Astar.AStarSearch((x_now//4,y_now//4),tuple(canteens_coord_downsample), astar_graph)
		routes=[[a[0]*4, a[1]*4]for a in routes_downsample] 
		pygame_display.draw_route(routes)
		#print ("route", result)
		route_costs.append(cost)
		route_paths.append(routes)
		print ("Location",i,"cost", cost)
		i+=1
	route_reward=-normalize_meanstd(route_costs)
	highest_reward_index=np.argmax(route_reward)
	pygame_display.display_default_img()
	pygame_display.route_text_message(wait=False)
	pygame_display.draw_route(route_paths[highest_reward_index])
	return route_reward,highest_reward_index

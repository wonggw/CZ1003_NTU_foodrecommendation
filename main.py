import pygame
import Algo
import Astar
from route_data import route_data
import display

pygame.init()
pygame.display.set_caption("Canteen")
pygame_display=display.pg_display()
pygame_display.display_welcome_img()
astar_graph=Astar.AStarGraph(route_data.Obstacles_mtx,route_data.bus_mtx,route_data.bus_stop_mtx)
while True:
	i=0
	x_now,y_now,map_coord_status=pygame_display.get_user_location()
	if map_coord_status==True:
		route_reward,highest_reward_index=Algo.distance_a_b(x_now,y_now,astar_graph,pygame_display)
		print (route_reward,highest_reward_index)

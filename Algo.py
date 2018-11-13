import numpy as np
import Astar
import display
import threading
import queue
from route_data import route_data

def KL(a, b):	#Kullback–Leibler divergence
	a = np.asarray(a, dtype=np.float)
	b = np.asarray(b, dtype=np.float)

	return np.sum(np.where(a != 0, a * np.log(a / b), 0))

def OVL_two_random_arr(arr1, arr2, number_bins): #Overlap coefficient
	# Determine the range over which the integration will occur
	arr1 = np.asarray(arr1, dtype=np.float)
	arr2 = np.asarray(arr2, dtype=np.float)
	min_value = np.min((min(arr1), min(arr2)))
	max_value = np.max((max(arr1), max(arr2)))
	# Determine the bin width
	bin_width = (max_value-min_value)/number_bins
	#For each bin, find min frequency
	lower_bound = min_value #Lower bound of the first bin is the min_value of both arrays
	min_arr = np.empty(number_bins) #Array that will collect the min frequency in each bin
	for b in range(number_bins):
		higher_bound = lower_bound + bin_width #Set the higher bound for the bin
		#Determine the share of samples in the interval
		freq_arr1 = np.ma.masked_where((arr1<lower_bound)|(arr1>=higher_bound), arr1).count()/len(arr1)
		freq_arr2 = np.ma.masked_where((arr2<lower_bound)|(arr2>=higher_bound), arr2).count()/len(arr2)
		#Conserve the lower frequency
		min_arr[b] = np.min((freq_arr1, freq_arr2))
		lower_bound = higher_bound #To move to the next range
	return min_arr.sum()

def normalize_meanstd(a, axis=None): 
	# axis param denotes axes along which mean & std reductions are to be performed
	mean = np.mean(a, axis=axis, keepdims=True)
	std = np.sqrt(((a - mean)**2).mean(axis=axis, keepdims=True))
	return (a - mean) / std

def Astar_process(user_coord,canteen_coord,canteens_name,astar_graph,pygame_display,queue):
	routes_downsample,cost =Astar.AStarSearch(user_coord,canteen_coord, astar_graph)
	routes=[[a[0]*4, a[1]*4]for a in routes_downsample] 
	pygame_display.draw_route(routes)
	queue.put({canteens_name:[routes_downsample,cost]})

def distance_a_b(x_now,y_now,astar_graph,pygame_display,canteens_coords,canteens_names):
	route_costs=[]
	route_paths=[]
	route_names=[]
	threads = []
	q = queue.Queue()
	canteens_coords_downsample=[[a[0]//4, a[1]//4] for a in canteens_coords] #downsample coordinate by 4
	pygame_display.shortest_route([])

	'''
	Create thread to calculate the shortest route based on user location with each canteen location
	'''
	threads = [threading.Thread(target = Astar_process, args =((x_now//4,y_now//4),tuple(canteens_coords_downsample[i]),canteens_names[i], astar_graph,pygame_display,q), daemon=True) for i in range(len(canteens_coords_downsample))]
	[t.start() for t in threads]
	[t.join() for t in threads]

	while not q.empty(): #collect all the value in queue
		canteen_dist = q.get()
		for key in canteen_dist:
			route_paths.append([[a[0]*4, a[1]*4]for a in canteen_dist[key][0]])
			route_costs.append(canteen_dist[key][1])
			route_names.append(key)

	route_reward=-normalize_meanstd(route_costs)
	highest_reward_index=np.argmax(route_reward)	#compute the index with the highest score
	pygame_display.display_default_img()
	pygame_display.shortest_route(route_paths[highest_reward_index],wait=False) #display route with the highest score
	return route_names,route_reward

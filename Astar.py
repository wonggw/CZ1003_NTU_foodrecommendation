from __future__ import print_function
import matplotlib.pyplot as plt
import route_data
 
class AStarGraph(object):
	#Define a class board like grid with two barriers
 
	def __init__(self,Obstacles_mtx,bus_mtx,bus_stop_mtx):
		self.barriers = []
		self.bus_routes = []
		self.bus_stops=[]
		self.width_graph=168
		self.height_graph=190
		self.barriers.append(Obstacles_mtx)
		self.bus_routes.append(bus_mtx)
		self.bus_stops.append(bus_stop_mtx)
 
	def heuristic(self, start, goal):
		#Use Chebyshev distance heuristic if we can move one square either
		#adjacent or diagonal
		D = 1
		D2 = 1
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
 
	def get_vertex_neighbours(self, pos):
		n = []
		#Moves allow link a chess king
		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < 0 or x2 > self.width_graph or y2 < 0 or y2 > self.height_graph:
				continue
			n.append((x2, y2))
		return n
 
	def move_cost(self, a, b):
		for barrier in self.barriers:
			if b in barrier:
				return 1000 #Extremely high cost to enter barrier squares
		for bus_route in self.bus_routes:
			if b in bus_route:
				return 3 #average walking speed of human 12.5m/s
		for bus_stop in self.bus_stops:
			if b in bus_stop:
				return 1
		return 27 #Normal movement cost, average walking speed of human 1.4m/s

def AStarSearch(start, end, graph):

	G = {} #Actual movement cost to each position from the start position
	F = {} #Estimated movement cost of start to end going via this position

	#Initialize starting values
	G[start] = 0 
	F[start] = graph.heuristic(start, end)

	closedVertices = set()
	openVertices = set([start])
	cameFrom = {}

	while len(openVertices) > 0:
		#Get the vertex in the open list with the lowest F score
		current = None
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				current = pos

		#Check if we have reached the goal
		if current == end:
			#Retrace our route backward
			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()
			return path, F[end] #Done!

		#Mark the current vertex as closed
		openVertices.remove(current)
		closedVertices.add(current)

		#Update scores for vertices near the current position
		for neighbour in graph.get_vertex_neighbours(current):
			if neighbour in closedVertices: 
				continue #We have already processed this node exhaustively
			candidateG = G[current] + graph.move_cost(current, neighbour)

			if neighbour not in openVertices:
				openVertices.add(neighbour) #Discovered a new vertex
			elif candidateG >= G[neighbour]:
				continue #This G score is worse than previously found

			#Adopt this G score
			cameFrom[neighbour] = current
			G[neighbour] = candidateG
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H

	raise RuntimeError("A* failed to find a solution")

if __name__=="__main__":
	#print(route_data.Obstacles_mtx)
	graph = AStarGraph(route_data.Obstacles_mtx,route_data.bus_mtx,route_data.bus_stop_mtx)
	result, cost = AStarSearch((40,70), (130,60), graph)
	#print ("route", result)
	#print ("cost", cost)
	plt.plot([v[0] for v in result], [v[1] for v in result])
	for barrier in graph.barriers:
		plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
	for bus_route in graph.bus_routes:
		plt.plot([v[0] for v in bus_route], [v[1] for v in bus_route])
	plt.xlim(-1,168)
	plt.ylim(-1,190)
	plt.show()

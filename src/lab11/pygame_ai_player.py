import sys
import pygame
import random
import heapq
import math

from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.turn_combat import CombatPlayer
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

# NOTICE: FOR THIS CODE TO WORK PROPERLY THE PLAYER MUST MOVE THEIR MOUSE ACROSS THE SCREEN.
# THIS IS FOR PYGAME TO RECOGNIZE THAT SOME SORT OF EVENT IS OCCURING AND TO PROCEED WITH THE CODE.
# I'VE TRIED USING TIMER EVENTS AND OTHER METHOD TO TRY AND AVOID THIS BUT I'VE HAD NO LUCK OF IT
# RUNNING CORRECTLY OR WITHOUT ERRORS

# Also the game will end if the AI chooses to go to city #9 so that we do not modify existing code

""" Create PyGameAIPlayer class here"""
class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        # Chooses a random city to go to and returns the corresponding key
        choice = random.randint(1, 10)
        choice -= 1
        if choice == 0:
            return pygame.K_0
        elif choice == 1:
            return pygame.K_1
        elif choice == 2:
            return pygame.K_2
        elif choice == 3:
            return pygame.K_3
        elif choice == 4:
            return pygame.K_4
        elif choice == 5:
            return pygame.K_5
        elif choice == 6:
            return pygame.K_6
        elif choice == 7:
            return pygame.K_7
        elif choice == 8:
            return pygame.K_8
        else:
            return pygame.K_9
    
    def recommendedAction(self, best_path, current_step, city_names):
        # What is the best city to go to for the current step?
        nextDestination = best_path[current_step]
        
        # What is the destination's index?
        choice = city_names.index(nextDestination)

        # Chooses a city to go to and returns the corresponding key
        if choice == 0:
            return pygame.K_0
        elif choice == 1:
            return pygame.K_1
        elif choice == 2:
            return pygame.K_2
        elif choice == 3:
            return pygame.K_3
        elif choice == 4:
            return pygame.K_4
        elif choice == 5:
            return pygame.K_5
        elif choice == 6:
            return pygame.K_6
        elif choice == 7:
            return pygame.K_7
        elif choice == 8:
            return pygame.K_8
        else:
            return pygame.K_9

    def dijkstra_algorithm(self, graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
    
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}
    
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0   
        shortest_path[start_node] = 0
        
        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
    
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        
        return previous_nodes, shortest_path

    def print_result(self, previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
    
        # Add the start node manually
        path.append(start_node)
        
        print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
        print(" -> ".join(reversed(path)))
        return path

    def translate_routes(self, cities, routes, city_names):
        # Create the dictionary that we'll use to assosiate city names with coordinates
        city_dict = { 
            cities[0]: city_names[0],
            cities[1]: city_names[1],
            cities[2]: city_names[2],
            cities[3]: city_names[3],
            cities[4]: city_names[4],
            cities[5]: city_names[5],
            cities[6]: city_names[6],
            cities[7]: city_names[7],
            cities[8]: city_names[8],
            cities[9]: city_names[9]
        }

        # "Renaming" the routes list so that code is easier to understand
        original_list = routes

        # Replace each tuple with the associated string
        new_list = []
        for tup in original_list:
            new_tup = []
            for item in tup:
                new_tup.append(city_dict[item])
            new_list.append(new_tup)

        return new_list 

    def create_graph(self, city_names, translated_routes):
        init_graph = {}
        for city_name in city_names:
            init_graph[city_name] = {}

        for route in translated_routes:
            init_graph[route[0]][route[1]] = random.randint(1,10)

        graph = Graph(city_names, init_graph)
        previous_nodes, shortest_path = self.dijkstra_algorithm(graph=graph, start_node=city_names[0])
        path = self.print_result(previous_nodes, shortest_path, start_node=city_names[0], target_node=city_names[-1])

        return path


""" Create PyGameAICombatPlayer class here"""
class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):               
        choice = random.randint(1, 3)
        self.weapon = choice - 1
        return self.weapon

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

if __name__ == '__main__':
    player = PyGameAIPlayer()

    # Convert what we have into a readable routes for the new algorithm
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]
    size = width, height = 640, 480
    cities = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(cities)
    random.shuffle(routes)
    routes = routes[:10]
    translated_routes = player.translate_routes(cities, routes, city_names)

    # Dijkstra's algorithm
    init_graph = {}
    for city_name in city_names:
        init_graph[city_name] = {}

    for route in translated_routes:
        init_graph[route[0]][route[1]] = random.randint(1,10)

    graph = Graph(city_names, init_graph)
    previous_nodes, shortest_path = player.dijkstra_algorithm(graph=graph, start_node=city_names[0])
    player.print_result(previous_nodes, shortest_path, start_node=city_names[0], target_node=city_names[-1])
        
''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''

import random
import itertools

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of cities with random x and y coordinates.
    """
    # Consider the condition where x size and y size are different
    cities = []
    for i in range(n_cities):
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        coordinates = (x,y)
        cities.append(coordinates)

    return cities

    pass

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of cities names
    :return: A list of tuples representing all possible links between cities, 
            each item in the list (a link) represents a route between two cities.
    """

    """
    a = ['a', 'b', 'c'] 

    for a_combinations in itertools.combinations(a,2):
        print(a_combinations)
    """


    routes = []
    for route_list in itertools.combinations(city_names,2):
        routes.append(route_list)

    return(routes)

    pass

def convert_to_graph(routes):
    graph = {}
    for start, end in routes:
        if start not in graph:
            graph[start] = {}
        if end not in graph[start]:
            graph[start][end] = random.randint(1, 10) # replace 10 with the maximum value you want for the random integer

    # Now that the graph has been created, replace each key with a string
    
    return graph

# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 100), 10)
    routes = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')


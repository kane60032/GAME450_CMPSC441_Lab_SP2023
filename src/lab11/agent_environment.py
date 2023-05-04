import sys
import pygame
import random
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from landscape import get_landscape, get_combat_bg
from pygame_ai_player import PyGameAIPlayer

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from lab7.ga_cities import run_lab_7

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes

if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "assets/lego.png"
    sprite_speed = 1

    # Stores the player's gold count (used when traveling along paths)
    starting_gold = 20
    current_gold = starting_gold

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface = get_landscape_surface(size)
    combat_surface = get_combat_surface(size)
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

    cities = get_randomly_spread_cities(size, len(city_names))
    ### IMPLEMENT GA_CITIES CODE RIGHT HERE
    #n_cities = len(city_names)
    #cities = run_lab_7(n_cities, size)

    # THIS IS WHERE THE LAB CONTINUES NORMALLY
    routes = get_routes(cities)

    random.shuffle(routes)
    routes = routes[:10]

    player_sprite = Sprite(sprite_path, cities[start_city])

    player = PyGameHumanPlayer()       # Use select_action on line 132 and comment out recommendedAction
    #player = PyGameAIPlayer()           # Use recommendedAction on line 133 comment out select_action

    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=cities,
        routes=routes,
    )

    """ THIS IS WHERE WE CHANGE IT SO THAT DIJSKTRA IS IMPLEMENTED """
    # Here's what happens
    # 1. We translate the routes list to use the city names instead of its coordinates
    # 2. Send the graph to the algorithm in pygame_ai_player so that the best path to take can be calculated
    # 3. Instead of selecting a random city to go to (ignoring paths), select the next city to go to based on where we are and the best path made
    translated_routes = player.translate_routes(cities, routes, city_names)
    best_path, graph = player.create_graph(city_names, translated_routes)
    current_step = len(best_path) - 1
    while True:
        #print("BEFORE CALLING SELECTACTION")
        action = player.selectAction(state, translated_routes, city_names)
        #print("AFTER CALLING SELECTACTION")
        #action = player.recommendedAction(best_path, current_step, city_names)

        # Move the "map" to the next city in the best route 
        if current_step != 0:
            current_step -= 1

        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                start = cities[state.current_city]
                state.destination_city = int(chr(action))
                destination = cities[state.destination_city]
                player_sprite.set_location(cities[state.current_city])
                state.travelling = True
                print(
                    "Travelling from", state.current_city, "to", state.destination_city
                )
                # Update the gold amount from traveling
                current_gold = player.pay_the_toll(current_gold, best_path, current_step, graph)
                print("Remaining Gold: ", current_gold)

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in cities:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(cities, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('You have reached the end of the game!')
            break

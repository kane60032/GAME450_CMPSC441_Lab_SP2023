import pygame
import random
from lab11.turn_combat import CombatPlayer

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            # Chooses a random city to go to and returns the corresponding key
            choice = random.randint(1, 10)
            choice -= 1
            if choice == 0:
                event.key = pygame.K_0
            elif choice == 1:
                event.key = pygame.K_1
            elif choice == 2:
                event.key = pygame.K_2
            elif choice == 3:
                event.key = pygame.K_3
            elif choice == 4:
                event.key = pygame.K_4
            elif choice == 5:
                event.key = pygame.K_5
            elif choice == 6:
                event.key = pygame.K_6
            elif choice == 7:
                event.key = pygame.K_7
            elif choice == 8:
                event.key = pygame.K_8
            else:
                event.key = pygame.K_9
                # We can end the game here since we aren't adding code elsewhere to check for an game endstate
                print("\n\n\tLegolas made it to the end! Quiting game...\n\n")
                pygame.quit()
            return event.key

        return ord(str(state.current_city))  # Not a safe operation for >10 cities


""" Create PyGameAICombatPlayer class here"""
class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                choice = random.randint(1, 3)
                self.weapon = choice - 1
                return self.weapon
                
                    #if event.key in [ord("s"), ord("a"), ord("f")]:
                    #    choice = {ord("s"): 1, ord("a"): 2, ord("f"): 3}[event.key]
                    #    self.weapon = choice - 1
                    #    return self.weapon

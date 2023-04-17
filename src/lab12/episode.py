''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''

import sys
from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.turn_combat import Combat
from lab11.pygame_combat import run_turn
from lab11.pygame_ai_player import PyGameAICombatPlayer

def run_episode(player, opponent):
    currentCombat = Combat()
    results = []
    while not currentCombat.gameOver:
        prevPlayerHealth = player.health
        prevOpponentHealth = opponent.health
        reward = run_turn(currentCombat, player, opponent)
        result = ((prevPlayerHealth, prevOpponentHealth), player.weapon, reward)
        #reward = run_turn(currentCombat, player, opponent)
        results.append(result)

    return results  # This is the history used in get_history_return

if __name__ == "__main__":
    player = PyGameAICombatPlayer("PLAYER AI")
    opponent = PyGameAICombatPlayer("OPPONENT AI")
    results = run_episode(player, opponent)

    for result in results:
        print(result)
        print('\n')

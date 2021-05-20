#
# License: See LICENSE.md file
# GitHub: https://github.com/Bobison/PyBoy
#
__pdoc__ = {
    "GameWrapperPokemonRed.cartridge_title": False,
    "GameWrapperPokemonRed.post_tick": False,
}

import logging

# Don't think we need this
import numpy as np
#nor this
from pyboy.utils import WindowEvent

from .base_plugin import PyBoyGameWrapper

logger = logging.getLogger(__name__)

try:
    from cython import compiled
    cythonmode = compiled
except ImportError:
    cythonmode = False

# D057 - Type of battle
ADDR_BATTLE_BIT = 0xD057
# D05A - Battle Type (Normal battle, Safari Zone, Old Man battle...)
# Pokedex Own Beginning
ADDR_POKEDEX_OWN = 0xD2F7
# Pokedex Seen Beginning
ADDR_POKEDEX_SEEN= 0xD30A

def load_mem_from(obj, mem, nbytes):
    arr = []
    for i in range(0, nbytes):
        arr[i] = obj.get_memory_value(mem + i)
    return arr

class GameWrapperPokemonRed(PyBoyGameWrapper):
    """
    """
    cartridge_title = "POKEMON RED"

    def __init__(self, *args, **kwargs):
        # I guess it should be full of unseens...
        # self.pokedex = {}
        # """Pokedex is empty"""

        # At first we are not in a fight
        self.isBattling = False
        """Boolean indicating if we are currently battling"""

        for i in range(0,19):
            self.pokedex_own[i] = 0
            self.pokedex_seen[i] = 0

    def load_pokedex(self):
        """
        Load pokedex have and seen
        """
        for i in range(0,19):
            self.pokedex_own[i] = self.pyboy.get_memory_value(ADDR_POKEDEX_OWN + i)
            self.pokedex_seen[i] = self.pyboy.get_memory_value(ADDR_POKEDEX_SEEN + i)

    def post_tick(self):
        # If there is a change in the battle status
        if self.isBattling != self.pyboy.get_memory_value(ADDR_BATTLE_BIT):
            self.isBattling = self.pyboy.get_memory_value(ADDR_BATTLE_BIT)
            self.load_pokedex()

    def start_game(self, timer_div=None):
        """
        Starts the game
        """
        PyBoyGameWrapper.start_game(self, timer_div=timer_div)

    # def reset_game(self, timer_div=None):
    #     """
    #     Resets the game
    #     """
    #     PyBoyGameWrapper.reset_game(self)

    # def game_over(self):
    #     # Apparantly that address is for game over
    #     # https://datacrystal.romhacking.net/wiki/Super_Mario_Land:RAM_map
    #     return self.pyboy.get_memory_value(0xC0A4) == 0x39

    # def __repr__(self):
    #     adjust = 4
        # yapf: disable

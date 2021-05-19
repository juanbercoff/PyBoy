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

# D057 is set to either 0 or 1 by the game itself, it's always 1 during battle and 0 outside of battle
ADDR_BATTLE_BIT = 0xD057


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

    def post_tick(self):
        # Setting bit after each tick
        self.isBattling = self.pyboy.get_memory_value(ADDR_BATTLE_BIT)

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

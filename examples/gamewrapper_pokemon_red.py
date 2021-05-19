#
# License: See LICENSE.md file
# GitHub: https://github.com/Bobison/PyBoy
#

import os
import sys

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

from pyboy import PyBoy, WindowEvent # isort:skip

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: python gamewrapper_pokemon_red.py [ROM file]")
    exit(1)

quiet = "--quiet" in sys.argv
pyboy = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=not quiet, game_wrapper=True)
pyboy.set_emulation_speed(0)
# not so sure about this... Check that
assert pyboy.cartridge_title() == "POKEMON RED"

pokemon = pyboy.game_wrapper()
assert pokemon != None
pokemon.start_game()

assert pokemon.isBattling == False

# print(pokemon)

while not pyboy.tick():
# pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    print(pokemon.isBattling)

pyboy.stop()

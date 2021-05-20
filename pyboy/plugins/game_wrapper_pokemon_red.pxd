#
# License: See LICENSE.md file
# GitHub: https://github.com/Bobison/PyBoy
#
from libc.stdint cimport uint8_t
from pyboy.plugins.base_plugin cimport PyBoyGameWrapper
cimport cython

cdef struct Pokemon:
  char Hp[2]
  char Lvl


cdef struct Player:
  char Name[4]
  Pokemon Party[6]

cdef class GameWrapperPokemonRed(PyBoyGameWrapper):
    # Variables
    # cdef public dict pokedex
    cdef public int isBattling
    # This is a BitMap of 19*8 = 152 pokemons
    cdef public char pokedex_own[19]
    cdef public char pokedex_seen[19]

    # Pokedex function
    # cpdef bool pokedex_seen(self, pokemon)
    # cpdef bool pokedex_have(self, pokemon)

    # Control functions
    cpdef void start_game(self, timer_div=*)

    # Load pokedex info after a fight
    cpdef void load_pokedex(self)
    # cpdef void reset_game(self, timer_div=*)
    # cpdef void stop_game(self)

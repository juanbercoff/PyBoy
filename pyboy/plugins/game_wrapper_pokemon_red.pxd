#
# License: See LICENSE.md file
# GitHub: https://github.com/Bobison/PyBoy
#
from libc.stdint cimport uint8_t
from pyboy.plugins.base_plugin cimport PyBoyGameWrapper
cimport cython

# Enum type for Pokemon
cdef enum Pokemon:
  Pikachu

cdef enum PokedexSt:
  Seen, Have, Nothing


cdef class GameWrapperPokemonRed(PyBoyGameWrapper):
    # Variables
    # cdef public dict pokedex
    cdef public int isBattling

    # Pokedex function
    # cpdef bool pokedex_seen(self, pokemon)
    # cpdef bool pokedex_have(self, pokemon)

    # Control functions
    cpdef void start_game(self, timer_div=*)
    # cpdef void reset_game(self, timer_div=*)
    # cpdef void stop_game(self)

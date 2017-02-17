from . import SCRAMBLE_222_SRC, MATHLIB_SRC, trim
import execjs

_scrambler = execjs.compile(MATHLIB_SRC + SCRAMBLE_222_SRC)

#------------------------------------------------------------------------------

@trim
def get_random_scramble():
    """ Gets a WCA random scramble (sub-optimal) of a 2x2x2 cube. """
    return _scrambler.call("scramble_222.getRandomScramble")

@trim
def get_optimal_scramble():
    """ Gets an optimal random state scramble of a 2x2x2 cube. """
    return _scrambler.call("scramble_222.getOptimalScramble")
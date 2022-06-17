#!/usr/bin/python3

import itertools
s = "eleetminicoworoep"
permutations = list(itertools.permutations(s))
print([''.join(permutation) for permutation in permutations])

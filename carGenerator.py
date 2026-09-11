import numpy as np
from numpy import random as rand

colour_dist = rand.choice(['White', 'Black', 'Gray', 'Silver', 'Blue', 'Red', 'Green', 'Brown', 'Orange', 'Gold', 'Purple'], 100, p = [.246, .217, .198, .141, .089, .075, .02, .009, .0031, .001, .0009])

print(colour_dist)

white = 0
black = 0
other = 0
for i in colour_dist:
    if i == 'White':
        white += 1
    elif i == 'Black':
        black += 1
    else:
        other += 1

print(white, black, other)
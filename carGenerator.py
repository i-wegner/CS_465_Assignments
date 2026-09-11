import numpy as np
from numpy import random as rand
import pandas as pd

rng = rand.default_rng(seed = 69)
colour_dist = rng.choice(['White', 'Black', 'Gray', 'Silver', 'Blue', 'Red', 'Green', 'Brown', 'Orange', 'Gold', 'Purple'], 100000, p = [.246, .217, .198, .141, .089, .075, .02, .009, .0031, .001, .0009])

colour_dist = pd.DataFrame(colour_dist, columns=['Colour'])
colour_dist.to_csv("cars-wegner.csv", index = False, header = False)
import numpy as np
from numpy import random as rand
import pandas as pd

rng = rand.default_rng(seed = 69)
colour_dist = rng.choice(['White', 'Black', 'Gray', 'Silver', 'Blue', 'Red', 'Green', 'Brown', 'Orange', 'Gold', 'Purple'], 100000, p = [.246, .217, .198, .141, .089, .075, .02, .009, .0031, .001, .0009])
model_dist = rng.choice(['Ford F-Series', 'Toyota RAV4', 'GMC Seirra', 'Honda CRV', 'Chevrolet Silverado', 'RAM 1500', 'Hyundai Tucson', 'Nissan Rogue', 'Ford Escape', 'Subaru Crosstrek'], 100000, p = [0.261, 0.131, 0.101, 0.096, 0.093, 0.073, 0.071, 0.061, 0.057, 0.056])

fordF = 0
toyota = 0
gmc = 0
honda = 0
chevy = 0
ram = 0
hyundai = 0
nissan = 0
fordE = 0
suby = 0

for row in model_dist:
    if row == 'Ford F-Series':
        fordF += 1
    elif row == 'Toyota RAV4':
        toyota +=1
    elif row == 'GMC Seirra':
        gmc +=1
    elif row == 'Honda CRV':
        honda+=1
    elif row == 'Chevrolet Silverado':
        chevy+=1
    elif row == 'RAM 1500':
        ram +=1
    elif row == 'Hyundai Tucson':
        hyundai+=1
    elif row == 'Nissan Rogue':
        nissan+=1
    elif row == 'Ford Escape':
        fordE +=1
    elif row == 'Subaru Crosstrek':
        suby +=1
    else:
        print('Something wrong here')

print(f'Ford F: {fordF}\n')
print(f'Toyota: {toyota}\n')
print(f'gmc: {gmc}\n')
print(f'honda: {honda}\n')
print(f'chevy: {chevy}\n')
print(f'ram: {ram}\n')
print(f'hyundai: {hyundai}\n')
print(f'nissan: {nissan}\n')
print(f'fordE: {fordE}\n')
print(f'Subaru: {suby}')


colour_dist = pd.DataFrame(colour_dist, columns=['Colour'])
colour_dist.to_csv("cars-wegner.csv", index = False, header = False)
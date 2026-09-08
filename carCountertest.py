import pandas as pd

df = pd.DataFrame(
    {
        'colour' : ['Black', 'Blue', 'Black', 'Blue', 'Black', 'Red', 'White', 'White', 'White', 'White', 'Silver', 'Gray', 'White', 'White', 'Silver', 'Gray', 'White', 'Green', 'Black', 'Black'],
        'model' : ['Tesla', 'Toyota', 'Ford', 'GMC', 'GMC', 'Honda', 'Toyota', 'RAM', 'Toyota', 'Ford', 'GMC', 'GMC', 'Tesla', 'RAM', 'RAM', 'GMC', 'Honda', 'Honda', 'Toyota', 'Toyota'],
    }
)

#df_colour = df[df.duplicated(subset='colour')]
s_model = df.duplicated(subset = 'model')

s_colour = df['colour'].drop_duplicates()
s_model = df['model'].drop_duplicates()

num_colours = 0
num_models = 0
colours_list = []
models_list = []

for index in s_colour:
    num_colours += 1
    colours_list.append(index)

for index in s_model:
    num_models += 1
    models_list.append(index)

first = df.iloc[0] # this saves the variable 'first' as a pandas series
second = df.iloc[1]

print(first.values[0], first.values[1]) #returns a pandas string array

cube = [[0] * num_models for i in range(num_colours)]
for row in cube:
    print(row)

print(id(cube[0]))
print(id(cube[1]))
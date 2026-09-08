import pandas as pd

df = pd.read_csv('cars-class.csv', header = None)
df = df.rename(columns={0:'Colour', 1:'Model'})

s_colour = df['Colour'].drop_duplicates() # Creates a pandas series with only the unique colours from df
s_model = df['Model'].drop_duplicates() # Creates a pandas series with only the unique models from df

num_colours = 0
colour_dict = {}

num_models = 0
model_dict = {}

for i in s_colour: # iterate over series
    colour_dict.update({num_colours : s_colour.iloc[num_colours]}) # add colour as value to dictionary paried with key = iteration #
    num_colours += 1 # increment num_colours by one
for i in s_model:
    model_dict.update({num_models : s_model.iloc[num_models]})
    num_models += 1

cube = [[0]*num_models]*num_colours # instantiate a 2d array (cube) with num_models columns and num_colours rows
# this is the problem with my program
# this instantiation essentially creates five copies of the same list and stores them in cube
# demonstrated:  
print(cube[0] is cube[2])
print(id(cube[0]))
print(id(cube[1]))
print(id(cube[3]))

for i in range(df.shape[0]):
    temp_colour = df.iloc[i, 0]
    temp_model = df.iloc[i, 1]
    temp_row = next(key for key, value in colour_dict.items() if value == temp_colour)
    temp_column = next(key for key, value in model_dict.items() if value == temp_model)
    cube[temp_row][temp_column] += 1



#for row in cube:
#    print(row)


# df.size returns rows*columns
# df.shape returns a tuple (rows, columns) and index [0] so that we just loop over the rows
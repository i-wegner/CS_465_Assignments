import pandas as pd

df = pd.read_csv('cars-class.csv', header = None)
df = df.rename(columns={0:'Colour', 1:'Model'})

s_colour = df['Colour'].drop_duplicates() # Creates a pandas series with only the unique colours from df
s_model = df['Model'].drop_duplicates() # Creates a pandas series with only the unique models from df

num_colours = 0
# colour_list = []
colour_dict = {}

num_models = 0
# model_list = []
model_dict = {}

for i in s_colour: # iterate over series
    #colour_list.append(i) # add index i to the list, final result will be a list with only the 
    colour_dict.update({num_colours : s_colour.iloc[num_colours]}) # add colour as value to dictionary paried with key = iteration #
    num_colours += 1 # 
for i in s_model:
    #model_list.append(i)
    model_dict.update({num_models : s_model.iloc[num_models]})
    num_models += 1

cube = [[0]*num_models]*num_colours

for row in cube:
    print(row)

for key in colour_dict:
    temp = df[df['Colour'] == colour_dict.get(key)]
    temp2 = df[df['Model'] == model_dict.get(key)]
    print(f'The number of {colour_dict.get(key)} cars is {temp.shape[0]}')
    print(f'The number of {model_dict.get(key)}\'s: {temp2.shape[0]}')

for i in range(df.shape[0]): # df.size returns rows*columns
                             # df.shape returns a tuple (rows, columns) and index [0] so that we just loop over the rows
    pass
    temp_colour = df.iloc[0]
    temp_model = df.iloc[1]



# Check each row of the dataframe and perform a reverse dictionary lookup to match the colour/model combination to
# their respective columns in the cube
# Then add one to the corresponding index
# update cube size to include marginal column and row
# sum over each row and column -> complete
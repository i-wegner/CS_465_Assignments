import pandas as pd

df = pd.read_csv('cars-class.csv', header = None)
df = df.rename(columns={0:'Colour', 1:'Model'})

s_colour = df['Colour'].drop_duplicates()
s_model = df['Model'].drop_duplicates()

num_colours = 0
colour_list = []
colour_dict = {}

num_models = 0
model_list = []
model_dict = {}

for i in s_colour:
    colour_list.append(i)
    colour_dict.update({num_colours : colour_list[num_colours]})
    num_colours += 1
for i in s_model:
    model_list.append(i)
    model_dict.update({num_models : model_list[num_models]})
    num_models += 1

print(f'There are {num_colours} distinct colours and {num_models} distinct models in the dataframe.\n')
print(f'The colours are: {colour_list}')
print(f'The models are: {model_list}')
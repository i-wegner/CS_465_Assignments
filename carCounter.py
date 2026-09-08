import pandas as pd

df = pd.read_csv('cars-class.csv', header = None)
df = df.rename(columns={0:'Colour', 1:'Model'})

s_colour = df['Colour'].drop_duplicates()
s_model = df['Model'].drop_duplicates()

num_colours = 0
num_models = 0

model_list = []
colour_list = []

for colour in s_colour:
    num_colours += 1
    colour_list.append(colour)
for model in s_model:
    num_models += 1
    model_list.append(model)

print(f'There are {num_colours} distinct colours and {num_models} distinct models in the dataframe.\n')
print(f'The colours are: {colour_list}')
print(f'The models are: {model_list}')

colour_dict = {}
for i in range(num_colours):
    colour_dict.update({i : colour_list[i]})

print(colour_dict)
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



print(colours_list)
print(models_list)
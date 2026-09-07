import pandas as pd

df = pd.DataFrame(
    {
        'colour' : ['Black', 'Blue', 'Black', 'Blue', 'Black', 'Red', 'White', 'White', 'White', 'White', 'Silver', 'Gray', 'White', 'White', 'Silver', 'Gray', 'White', 'Green', 'Black', 'Black'],
        'model' : ['Tesla', 'Toyota', 'Ford', 'GMC', 'GMC', 'Honda', 'Toyota', 'RAM', 'Toyota', 'Ford', 'GMC', 'GMC', 'Tesla', 'RAM', 'RAM', 'GMC', 'Honda', 'Honda', 'Toyota', 'Toyota'],
    }
)

#df_colour = df[df.duplicated(subset='colour')]
df_model = df.duplicated(subset = 'model')

df_colour = df['colour'].drop_duplicates()

num_colours = 0
colours_list = []
for i in range(len(df_colour)):
    num_colours += 1
    print(df_colour.iloc(i))
    #colours_list.append(df_colour[i])

#print(df_model)
print(colours_list)
#print(type(df_model))

rows = []

#use df.drop_duplicates
#iterate through to get specfic colours
#repeat for models
#build cube
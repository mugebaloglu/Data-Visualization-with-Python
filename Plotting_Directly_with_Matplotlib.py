import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
print('Data read into a pandas dataframe!')
print(df_can.head())

df_can.set_index('Country', inplace=True)
print(df_can.head())

years = list(map(str, range(1980, 2014)))

#creating df with only years columns from 1980 - 2013
df_line=df_can[years]

#Applying sum to get total immigrants year-wise
total_immigrants=df_line.sum()
total_immigrants

#Create figure and axes
fig, ax = plt.subplots()
# Plot the line
ax.plot(total_immigrants)
ax.set_title('Immigrants between 1980 to 2013') 
ax.set_xlabel('Years')
ax.set_ylabel('Total Immigrants')
plt.show()

#CUSTOMIZE

#Create figure and axes
fig, ax = plt.subplots()

#Changing the index type to integer
total_immigrants.index = total_immigrants.index.map(int)

# Customizing the appearance of Plot
ax.plot(total_immigrants, 
        marker='s', #Including markers in squares shapes
        markersize=5, #Setting the size of the marker
        color='green', #Changing the color of the line
        linestyle="dotted") #Changing the line style to a Dotted line
#Setting up the Title
ax.set_title('Immigrants between 1980 to 2013') 

#Setting up the Labels
ax.set_xlabel('Years')
ax.set_ylabel('Total Immigrants')
ax.legend(['Immigrants'])

plt.show()

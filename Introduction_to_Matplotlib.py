import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

print('Data read into a pandas dataframe!')
print(df_can.head())

df_can.set_index('Country', inplace=True)



#In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake. The quake caused widespread devastation and loss of life and about three million people were affected by this natural disaster. 
#As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti. We can quickly visualize this effort using a Line plot:
#Question: Plot a line graph of immigration from Haiti using df.plot().

years = list(map(str, range(1980, 2014)))
#creating data series
haiti = df_can.loc['Haiti', years] 
print(haiti.head())
haiti.plot()

haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() 

#We can clearly notice how number of immigrants from Haiti spiked up from 2010 as Canada stepped up its efforts to accept refugees from Haiti.
#Let's annotate this spike in the plot by using the plt.text() method.

haiti.index = haiti.index.map(int) 
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 

#Question: Let's compare the number of immigrants from India and China from 1980 to 2013.

df_CI = df_can.loc[['India', 'China'], years]
df_CI

df_CI = df_CI.transpose()
df_CI.head()

df_CI.index = df_CI.index.map(int) 
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


#Question: Compare the trend of top 5 countries that contributed the most to immigration to Canada.

inplace = True 
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 
print(df_top5)


df_top5.index = df_top5.index.map(int) 
df_top5.plot(kind='line', figsize=(14, 8)) 



plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()